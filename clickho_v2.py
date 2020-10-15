import tkinter
import pyautogui as pa
import math
import random

job = None
counter = 0
worked_tasks = 0
tasks_to_submit = 0

submit_pos = None
dropdown_pos = None



def autoclick():
    global job
    global counter
    global submit_pos

    if not submit_pos:
        autoclick_label['text'] = "You have to set the submit position first!"
        return

    # actual autoclick logic
    pa.moveTo(submit_pos, duration=1)
    pa.click(submit_pos)


        # increment the task count
    counter += 1
    autoclick_label['text'] = "submitted " + str(counter) + " tasks"

    try:
        wait_time = int(autoclick_textbox.get()) * 1000
        if wait_time is None:
            raise UnboundLocalError
        autoclick_textbox["state"] = "disabled"
        work_to_end_textbox["state"] = "disabled"

    except ValueError or UnboundLocalError:
        autoclick_label['text'] = "Enter a meaningful number of seconds!"
        return

    job = root.after(wait_time, autoclick)
    return


def work_to_end():
    global job
    global worked_tasks
    global tasks_to_submit

    if not (work_to_end_textbox["state"] == "disabled"):
        try:
            worked_tasks = int(work_to_end_textbox.get())
            # get number of tasks to rph
            tasks_to_submit = math.ceil(worked_tasks * 1.5 / 4)
            work_to_end_textbox.delete(0, "end")
            autoclick_textbox["state"] = "disabled"
            work_to_end_textbox["state"] = "disabled"

        except ValueError:
            work_to_end_label['text'] = "Enter a meaningful number of tasks!"
            return

    if not (dropdown_pos or submit_pos):
        work_to_end_label['text'] = "You have to set the button positions first!"
        return

    work_to_end_label['text'] = "Working randomly!"
    ETA = tasks_to_submit * 4
    feedback_label["text"] = str(tasks_to_submit) + " tasks remaining. ETA: " + str(ETA) + " mins"

    job = root.after(1, work_to_end)

    # move randomly to mimic a real user
    pa.moveTo(random.randrange(0, 400), random.randrange(0, 400), duration=random.randrange(1, 4))

    pa.moveTo(dropdown_pos, duration=1)
    pa.typewrite(str(random.randrange(1, 6)))
    pa.typewrite("enter")
    pa.moveTo(submit_pos, duration=random.randrange(1, 4))
    pa.click(submit_pos)
    pa.moveTo(random.randrange(0, 400), random.randrange(0, 400), duration=random.randrange(1, 4))

    tasks_to_submit -= 1
    if tasks_to_submit == 0:
        feedback_label["text"] = "You've finished working randomly!"
        stop()
    return


def set_dropdown_position():
    global job
    global dropdown_pos
    job = root.after(5000)
    dropdown_pos = pa.position()
    feedback_label["text"] = "Successfully set dropdown button to: " + str(dropdown_pos)
    return


def set_submit_position():
    global job
    global submit_pos
    job = root.after(5000)
    submit_pos = pa.position()
    feedback_label["text"] = "Successfully set submit button to: " + str(submit_pos)
    return

def stop():
    global job
    if job:
        root.after_cancel(job)
        autoclick_textbox["state"] = "normal"
        work_to_end_textbox["state"] = "normal"
    return


root = tkinter.Tk()
autoclick_button = tkinter.Button(root, text="autoclick", command=autoclick)
autoclick_label = tkinter.Label(root, text="enter seconds to wait")
autoclick_textbox = tkinter.Entry(root, width=5)
autoclick_button.grid(row=0, column=0)
autoclick_label.grid(row=0, column=1)
autoclick_textbox.grid(row=0, column=2)

work_to_end_button = tkinter.Button(root, text="work to end", command=work_to_end)
work_to_end_label = tkinter.Label(root, text="enter the number of tasks you submitted")
work_to_end_textbox = tkinter.Entry(root, width=5)

work_to_end_button.grid(row=1, column=0)
work_to_end_label.grid(row=1, column=1)
work_to_end_textbox.grid(row=1, column=2)

stop_button = tkinter.Button(root, text="stop", command=stop)
stop_button.grid(row=2, column=2)

set_submit_button = tkinter.Button(root, text="set submit", command=set_submit_position)
set_dropdown_button = tkinter.Button(root, text="set dropdown", command=set_dropdown_position)
set_submit_button.grid(row=2, column=0)
set_dropdown_button.grid(row=2, column=1)

feedback_label = tkinter.Label(root, text="You will get some feedback here")
feedback_label.grid(row=3, column=1)

tkinter.mainloop()
