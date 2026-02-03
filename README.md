# django-signals-assignment
# Django Signals Demonstration

This Django project demonstrates the behavior of **Django Signals** for learning purposes.

## Questions Addressed

### 1. Are Django Signals synchronous or asynchronous?
By default, Django signals are **synchronous**.  
The `post_save` signal blocks the caller until it completes.

**Evidence:**  
In `core/signals.py`, `my_model_post_save` sleeps for 2 seconds.  
When visiting `/create/`, the HTTP response waits until the signal finishes.

---

### 2. Do Django Signals run in the same thread as the caller?
Yes, they run in the **same thread**.  
Both the view and signal print the thread name:

