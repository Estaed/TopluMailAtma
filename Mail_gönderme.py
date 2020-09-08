import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QLineEdit,QTextEdit,QGridLayout,QPushButton
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        self.kullanıcı_adı_yazı = QLabel("Mail Adresiniz:")
        self.parola_yazı = QLabel("Parolanız:")
        self.kullanıcı_adı = QLineEdit()
        self.parola = QLineEdit()
        self.parola.setEchoMode(QLineEdit.Password)

        self.atılacak_mailler_yazı = QLabel("Atılacak Mailler:")
        self.atılacak_mailler = QTextEdit()

        self.yazılacak_metin_yazı = QLabel("Yazılacak Metin:")
        self.yazılacak_metin = QTextEdit()



        self.gönder = QPushButton("Gönder")


        grid.addWidget(self.kullanıcı_adı_yazı,1,0)
        grid.addWidget(self.kullanıcı_adı,1,1)
        grid.addWidget(self.parola_yazı,2,0)
        grid.addWidget(self.parola,2,1)

        grid.addWidget(self.atılacak_mailler_yazı,3,0)
        grid.addWidget(self.atılacak_mailler,3,1)

        grid.addWidget(self.yazılacak_metin_yazı,4,0)
        grid.addWidget(self.yazılacak_metin,4,1)

        grid.addWidget(self.gönder,5,1)


        self.setLayout(grid)
        self.setWindowTitle("Mail Atma Programı")
        self.gönder.clicked.connect(self.mail_at)
        self.show()


    def mail_at(self):

        kullanıcı_adı = self.kullanıcı_adı.text()
        parola = self.parola.text()
        atılacak_mailler = self.atılacak_mailler.toPlainText()
        yazılacak_metin = self.yazılacak_metin.toPlainText()

        liste2 = list()
        liste2 = atılacak_mailler.split("*")

        mesaj = MIMEMultipart()


        for mail in liste2:
            mesaj["From"] = kullanıcı_adı

            mesaj["To"] = mail

            mesaj["Subject"] = "Smtp Mail Gönderme"

            mesaj_govdesi = MIMEText(yazılacak_metin, "plain")
            mesaj.attach(mesaj_govdesi)

            try:
                mail = smtplib.SMTP("Smtp.gmail.com",587)

                mail.ehlo()
                mail.starttls()

                mail.login(kullanıcı_adı, parola)

                mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())

                print("Mail Başarılıyla Gönderildi....")

                mail.close()

            except:
                sys.stderr.write("Bir Sorun Oluştu!")
                sys.stderr.flush()

        pencere.close()




app = QApplication(sys.argv)
pencere = Pencere()
pencere.setGeometry(100,100,500,300)
sys.exit(app.exec_())