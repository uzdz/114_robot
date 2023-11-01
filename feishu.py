from dingtalkchatbot.chatbot import DingtalkChatbot
import requests
import logging
import json
import time
import urllib3
urllib3.disable_warnings()

try:
    JSONDecodeError = json.decoder.JSONDecodeError
except AttributeError:
    JSONDecodeError = ValueError


def is_not_null_and_blank_str(content):
    """
    非空字符串
    :param content: 字符串
    :return: 非空 - True，空 - False
    """
    if content and content.strip():
        return True
    else:
        return False


class FeiShutalkChatbot(object):
    def __init__(self, webhook, secret=None, pc_slide=False, fail_notice=False):
        '''
        机器人初始化
        :param webhook: 飞书群自定义机器人webhook地址
        :param secret: 机器人安全设置页面勾选“加签”时需要传入的密钥
        :param pc_slide: 消息链接打开方式，默认False为浏览器打开，设置为True时为PC端侧边栏打开
        :param fail_notice: 消息发送失败提醒，默认为False不提醒，开发者可以根据返回的消息发送结果自行判断和处理
        '''
        super(FeiShutalkChatbot, self).__init__()
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}
        self.webhook = webhook
        self.secret = secret
        self.pc_slide = pc_slide
        self.fail_notice = fail_notice

    def send_text(self, msg, open_id=[]):
        """
        消息类型为text类型
        :param msg: 消息内容
        :return: 返回消息发送结果
        """
        data = {"msg_type": "text", "at": {}}
        if is_not_null_and_blank_str(msg):  # 传入msg非空
            data["content"] = {"text": msg}
        else:
            logging.error("text类型，消息内容不能为空！")
            raise ValueError("text类型，消息内容不能为空！")

        logging.debug('text类型：%s' % data)
        return self.post(data)

    def post(self, data):
        """
        发送消息（内容UTF-8编码）
        :param data: 消息数据（字典）
        :return: 返回消息发送结果
        """
        try:
            post_data = json.dumps(data)
            response = requests.post(self.webhook, headers=self.headers, data=post_data, verify=False)
        except requests.exceptions.HTTPError as exc:
            logging.error("消息发送失败， HTTP error: %d, reason: %s" % (exc.response.status_code, exc.response.reason))
            raise
        except requests.exceptions.ConnectionError:
            logging.error("消息发送失败，HTTP connection error!")
            raise
        except requests.exceptions.Timeout:
            logging.error("消息发送失败，Timeout error!")
            raise
        except requests.exceptions.RequestException:
            logging.error("消息发送失败, Request Exception!")
            raise
        else:
            try:
                result = response.json()
            except JSONDecodeError:
                logging.error("服务器响应异常，状态码：%s，响应内容：%s" % (response.status_code, response.text))
                return {'errcode': 500, 'errmsg': '服务器响应异常'}
            else:
                logging.debug('发送结果：%s' % result)
                # 消息发送失败提醒（errcode 不为 0，表示消息发送异常），默认不提醒，开发者可以根据返回的消息发送结果自行判断和处理
                if self.fail_notice and result.get('errcode', True):
                    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                    error_data = {
                        "msgtype": "text",
                        "text": {
                            "content": "[注意-自动通知]飞书机器人消息发送失败，时间：%s，原因：%s，请及时跟进，谢谢!" % (
                                time_now, result['errmsg'] if result.get('errmsg', False) else '未知异常')
                        },
                        "at": {
                            "isAtAll": False
                        }
                    }
                    logging.error("消息发送失败，自动通知：%s" % error_data)
                    requests.post(self.webhook, headers=self.headers, data=json.dumps(error_data))
                return result


def send(mark_available=list, webhook=str):
    # webhook 通过飞书群添加机器人可获取
    if webhook == '':
        return

    feishu = FeiShutalkChatbot(webhook)

    if mark_available is None:
        return

    if isinstance(mark_available, list):

        if len(mark_available) <= 0:
            return

        for single in mark_available:
            hos_name = single["hosName"]
            first_dept_name = single["firstDeptName"]
            second_dept_name = single["secondDeptName"]
            search_url = single["search_url"]
            yuyue = single["yuyue"]

            if len(yuyue) <= 0:
                continue

            content = '%s | %s | %s \n' % (hos_name, first_dept_name, second_dept_name)
            content = content + "".join(yuyue)

            rich_text = {
                "msg_type": "post",
                "content": {
                    "post": {
                        "zh_cn": {
                            "title": "[114] 可预约提醒：",
                            "content": [
                                [
                                    {
                                        "tag": "text",
                                        "text": content
                                    },
                                    {
                                        "tag": "a",
                                        "text": "点击查看",
                                        "href": search_url
                                    }
                                ]
                            ]
                        }
                    }
                }
            }

            feishu.post(rich_text)
