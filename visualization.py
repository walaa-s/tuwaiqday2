import pandas as pd
import matplotlib.pyplot as plt

# قراءة بيانات الطلاب من ملف Excel (أو CSV إذا كنتِ تستخدمينه)
df = pd.read_csv("student_info.csv")  # أو استخدمي pd.read_csv("student_info.csv") حسب نوع الملف

# حساب عدد الطلاب لكل تقدير (Grade)
grade_counts = df['Grade'].value_counts()

# الرسم البياني
plt.figure(figsize=(8, 6))
grade_counts.plot(kind='bar', color='lightgreen')
plt.title('Number of Students by Grade')
plt.xlabel('Grade')
plt.ylabel('Number of Students')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# عرض الرسم
plt.tight_layout()
plt.show()
