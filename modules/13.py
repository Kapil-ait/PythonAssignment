from reportlab.pdfgen import canvas

pdf = canvas.Canvas("student_report.pdf")

pdf.setTitle("Student Report")

pdf.drawString(100, 750, "STUDENT REPORT")
pdf.drawString(100, 700, "Name: Kapil Patidar")
pdf.drawString(100, 670, "Course: B.Tech CSE")
pdf.drawString(100, 640, "Marks: 85")
pdf.drawString(100, 610, "Result: PASS")

pdf.save()

print("PDF created successfully")