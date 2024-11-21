# Backup MySQL Database (Auto Backup)

این برنامه به‌طور خودکار از پایگاه‌داده MySQL بکاپ می‌گیرد. شما می‌توانید زمان‌بندی بکاپ‌ها را تنظیم کنید و برنامه به‌طور مداوم هر چند دقیقه یک‌بار از پایگاه‌داده شما بکاپ می‌گیرد.

## نصب و راه‌اندازی

### پیش‌نیازها
برای استفاده از این برنامه، باید موارد زیر را در سیستم خود نصب کرده باشید:

- Python 3.x
- MySQL
- کتابخانه‌های پایتون:
  - `pymysql`
  - `schedule`

### مراحل نصب

1. **نصب موارد مورد نیاز**
   ابتدا دستور زیر را در ترمینال وارد کنید تا کتابخانه‌های مورد نیاز نصب شوند:

   ```bash
   pip install pymysql schedule
   ```
2. **کانفیگ کردن**


برای تنظیم زمان‌بندی بکاپ و اطلاعات اتصال به پایگاه‌داده، باید مقادیر زیر را در فایل پایتون (sql.py) تنظیم کنید:

نام کاربری (db_user) پایگاه‌داده MySQL (به‌عنوان مثال 'root').

رمز عبور (db_password) پایگاه‌داده MySQL (در صورتی که ندارد خالی بگذارید '').

نام پایگاه‌داده‌ای (db_name) که می‌خواهید از آن بکاپ بگیرید (به‌عنوان مثال 'mtaserver').

آدرس سرور (db_host) پایگاه‌داده (اگر MySQL در سیستم محلی است، 'localhost' را وارد کنید).

مسیر پوشه‌ای (backup_dir) که می‌خواهید فایل‌های بکاپ در آن ذخیره شوند.

مقدار زمان‌بندی (interval_minutes) بکاپ‌ها به دقیقه. به‌عنوان مثال، اگر می‌خواهید بکاپ‌ها هر 10 دقیقه گرفته شوند، عدد 10 را وارد کنید.
