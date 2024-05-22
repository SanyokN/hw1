import email_sender


def main():
    inner_html_body = email_sender.create_welcome_letter(
        {
            'name': 'Sanyok',
            'hobbies': ['programming', 'computer games'],
            'has_car': False
        }
    )
    print(inner_html_body)
    email_sender.send_email(
        ["oleksandrnik@ukr.net"],
        mail_body=inner_html_body,
        mail_subject="hw5",
        attachment='Makefile',
    )


if __name__ == "__main__":
    main()
