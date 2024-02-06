import click
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

@click.command()
@click.option('--email', prompt='Введите вашу почту', help='Email для отправки уведомлений')
@click.option('--password', prompt=True, hide_input=True, help='Пароль от вашей почты')
@click.option('--recipient', prompt=True, help='Email получателя уведомлений')
@click.option('--message', prompt=True, help='Текст уведомления')
def send_weekly_reminder(email, password, recipient, message):
    # Подключение к SMTP серверу
    smtp_server = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()

    try:
        server.login(email, password)

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = recipient
        msg['Subject'] = 'Еженедельное напоминание'

        msg.attach(MIMEText(message, 'plain'))

        server.sendmail(email, recipient, msg.as_string())
        click.echo('Уведомление успешно отправлено!')
    except Exception as e:
        click.echo(f'Произошла ошибка при отправке уведомления: {str(e)}')
    finally:
        server.quit()

if __name__ == '__main__':
    send_weekly_reminder()
