from channels.consumer import SyncConsumer

class BG_Task(SyncConsumer):
    def count_to(self, event):
        print('yay')
        count = event.get('count', False)
        if not count:
            print('no usable data')
            return

        for i in range(count):
            print("value", i, "of", count)
