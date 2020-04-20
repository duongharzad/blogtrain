from django.db import models


# Create your models here.
class StudentModel(models.Model):
    name_student = models.CharField(max_length=255, null=True, blank=True, unique=False)
    sex = models.CharField(max_length=255, null=True, blank=True, unique=False)
    date = models.CharField(max_length=255, null=True, blank=True, unique=False)
    address = models.CharField(max_length=255, null=True, blank=True, unique=False)

    class Meta:
        db_table = 'Student'
        verbose_name = 'Student'

    def __str__(self):
        return self.name_student


class SubjectsModel(models.Model):
    name_subjects = models.CharField(max_length=255, null=True, blank=True, unique=False)

    credit_number = models.IntegerField(default=1)

    def __str__(self):
        return self.name_subjects

    class Meta:
        db_table = 'Subjects'
        verbose_name = 'Subjects'


class ScoreModel(models.Model):
    semester = models.CharField(max_length=255, null=True, blank=True, unique=False)
    test_score = models.IntegerField(default=0)
    subject_id = models.ForeignKey(SubjectsModel, null=True, blank=True, on_delete=models.DO_NOTHING)
    student_id = models.ForeignKey(StudentModel, null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'Score'
        verbose_name = 'Score'


class CourseModel(models.Model):
    name_course = models.CharField(max_length=255, null=True, blank=True, unique=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name_course

    class Meta:
        db_table = 'Course'
        verbose_name = 'Course'


class TrainingSystemModel(models.Model):
    name_training = models.CharField(max_length=255, null=True, blank=True, unique=False)

    class Meta:
        db_table = 'TrainingSystem'
        verbose_name = 'TrainingSystem'

    def __str__(self):
        return self.name_training


class FacultyModel(models.Model):
    name_faculty = models.CharField(max_length=255, null=True, blank=True, unique=False)
    address = models.CharField(max_length=255, null=True, blank=True, unique=False)

    class Meta:
        db_table = 'Faculty'
        verbose_name = 'Faculty'

    def __str__(self):
        return self.name_faculty


class ClassModel(models.Model):
    name_class = models.CharField(max_length=255, null=True, blank=True, unique=False)
    course_id = models.ForeignKey(CourseModel, null=True, blank=True, on_delete=models.DO_NOTHING)
    training_system_id = models.ForeignKey(TrainingSystemModel, null=True, blank=True, on_delete=models.DO_NOTHING)
    faculty_id = models.ForeignKey(FacultyModel, null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'Class'
        verbose_name = 'Class'

    def __str__(self):
        return self.name_class
