from dingtalkchatbot.chatbot import DingtalkChatbot


def create_monitor_flow(content):
    # webhook 通过钉钉群添加机器人可获取
    webhook = 'xxx'
    xiaoding = DingtalkChatbot(webhook)
    xiaoding.send_markdown(title='数据监控', text=content, is_at_all=True)


def send(mark_available=list):
    if mark_available is None:
        return

    if isinstance(mark_available, list):

        if len(mark_available) <= 0:
            return

        for single in mark_available:
            hos_name = single["hosName"]
            first_dept_name = single["firstDeptName"]
            second_dept_name = single["secondDeptName"]
            yuyue = single["yuyue"]

            if len(yuyue) <= 0:
                continue

            content = '#### ****[114] 可预约提醒 %s**** \n  *****%s***** - *****%s***** \n' % (hos_name, first_dept_name, second_dept_name)
            content = content + "".join(yuyue)

            create_monitor_flow(content)
