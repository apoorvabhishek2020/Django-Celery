from celery import shared_task


@shared_task
def sharedtask():
    print("Running Shared Task")
    return 5050
