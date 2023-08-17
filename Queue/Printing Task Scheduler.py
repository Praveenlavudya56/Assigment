# class Print:
#     def __init__(self):
#         self.printingTasks = []

#     def addPrintTaskToSchedule(self,printTask):
#         self.printingTasks.append(printTask)
#         print(f"Added task : {printTask}")

#     def printingTheTask(self):
#         if len(self.printingTasks) == 0:
#             print("No Tasks")
#             return
#         else:
#             while self.printingTasks:
#                 printTask = self.printingTasks.pop(0)
#                 print(f"printing: {printTask}")


# printScheduler = Print()

# printScheduler.addPrintTaskToSchedule("Sravya's resume")
# printScheduler.addPrintTaskToSchedule("Krishna's wiki page for telengana tourism")
# printScheduler.addPrintTaskToSchedule("Bindu's Mahesh Babu poster")

# printScheduler.printingTheTask()

#---------------------------------------------------------------------------------------------
#task is add a lmaxLength of 5, and do the same operation like the task above.
class Print:
    def __init__(self):
        self.printingTasks = []
        self.max_tasks = 5

    def addPrintTaskToSchedule(self, printTask):
        if len(self.printingTasks) < self.max_tasks:
            self.printingTasks.append(printTask)
            print(f"Added task: {printTask}")
        else:
            print("Schedule is full. Cannot add more tasks.")

    def printingTheTask(self):
        if len(self.printingTasks) == 0:
            print("No Tasks")
            return
        else:
            while self.printingTasks:
                printTask = self.printingTasks.pop(0)
                print(f"Printing: {printTask}")


printScheduler = Print()

# printScheduler.addPrintTaskToSchedule("Sravya's resume")
# printScheduler.addPrintTaskToSchedule("Krishna's wiki page for Telangana tourism")
# printScheduler.addPrintTaskToSchedule("Bindu's Mahesh Babu poster")
printScheduler.addPrintTaskToSchedule("Samantha's photography portfolio")
printScheduler.addPrintTaskToSchedule("Rajesh's business proposal")
printScheduler.addPrintTaskToSchedule("Priya's recipe book")
printScheduler.addPrintTaskToSchedule("Vijay's movie poster")

printScheduler.printingTheTask()
