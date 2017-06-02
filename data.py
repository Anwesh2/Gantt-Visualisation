import pandas as pd

df = pd.DataFrame([dict(Task="Job-1", Start='2017-01-01', Finish='2017-01-20', Resource='Complete'),
      dict(Task="Job-1", Start='2017-01-21', Finish='2017-04-21', Resource='Complete'),
      dict(Task="Job-1", Start='2017-04-22', Finish='2017-07-22', Resource='0-25'),
      dict(Task="Job-1", Start='2017-07-23', Finish='2017-08-23', Resource='Not_Started'),
      dict(Task="Job-1", Start='2017-08-24', Finish='2017-11-15', Resource='Not_Started'),
      dict(Task="Job-2", Start='2017-02-01', Finish='2017-02-15', Resource='Complete'),
      dict(Task="Job-2", Start='2017-02-16', Finish='2017-03-16', Resource='Complete'),
      dict(Task="Job-2", Start='2017-03-17', Finish='2017-04-10', Resource='Complete'),
      dict(Task="Job-2", Start='2017-04-11', Finish='2017-06-28', Resource='25-50'),
      dict(Task="Job-2", Start='2017-06-29', Finish='2017-07-15', Resource='Not_Started'),
      dict(Task="Job-3", Start='2017-03-10', Finish='2017-03-20', Resource='Complete'),
      dict(Task="Job-3", Start='2017-03-21', Finish='2017-06-25', Resource='50-75'),
      dict(Task="Job-3", Start='2017-06-26', Finish='2017-07-20', Resource='Not_Started'),
      dict(Task="Job-3", Start='2017-07-21', Finish='2017-10-05', Resource='Not_Started'),
      dict(Task="Job-4", Start='2017-01-15', Finish='2017-03-15', Resource='Complete'),
      dict(Task="Job-4", Start='2017-03-16', Finish='2017-06-15', Resource='75-100'),
      dict(Task="Job-4", Start='2017-06-16', Finish='2017-08-31', Resource='Not_Started')])

writer = pd.ExcelWriter('gantt.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()