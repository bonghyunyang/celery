from celery import shared_task


@shared_task
def test_task(a: int, b: int):
    print("test Celery task : ", a + b)
    return a + b

@shared_task
def test_periodic_task():
    print("test Periodic task")
    return "Complete"