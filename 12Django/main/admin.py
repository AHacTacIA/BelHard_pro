from django.contrib import admin

from main.models import Course, Students, Mark


# admin.site.register(Course)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'sex', 'active', 'short_name','student_courses')
    search_fields = ('name', 'surname')
    list_filter = ('sex',)

    def short_name(self, obj):
        return f"{obj.surname} {obj.name[0]}."

    def student_courses(self, obj):
        return ", ".join([str(course) for course in obj.course.all()])

    short_name.short_description = 'Короткое имя'
    student_courses.short_description = 'Курсы'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_num', 'start_date', 'end_date', 'description')
    search_fields = ('name', 'start_date', 'end_date')

    # def student_on(self,obj):
    #     return ", ".join([str(student) for course in obj.course.all()])
    # list_filter = ('sex',)

    # def short_name(self, obj):
    #     return f"{obj.surname} {obj.name[0]}."
    #
    # short_name.short_description = 'Короткое имя'


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('mark', 'student_name', 'course_name')

    def course_name(self, obj):
        return obj.course

    def student_name(self, obj):
        return f"{obj.student.name} {obj.student.surname}"

    course_name.short_description = 'Курс'
    student_name.short_description = 'Студент'