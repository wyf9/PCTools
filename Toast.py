from plyer import notification


def show_toast(title, message):
    '''
    显示 toast 消息
    '''
    notification.notify(
        title=title,
        message=message,
        app_name='PCTools',
        timeout=5
    )
    print("Toast通知:", message)


if __name__ == "__main__":
    show_toast("Test", "1111")
