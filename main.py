from __future__ import print_function

from DBUtils.databaseConnect import DBConnect
from DataTransformUtils.ParserUtils.MailParsers import BenzingaMailParse as bz
from EmailUtils import GmailUtils as GmailUtil

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    GM = GmailUtil.GmailService()
    results = GM.GetMessageList('from:benzinga',pagetoken=None)

    for messageId in results['messages']:
        messageId = messageId['id']
        messageBody = GM.GetMimeMessage(messageId)
        BZMessage = bz.BzMessage(messageBody)
        print(BZMessage.GetTickersFromMail())

    results2 = GM.GetMessageList('from:benzinga', pagetoken=results['nextPageToken'])

    for messageId in results2['messages']:
        messageId = messageId['id']
        messageBody = GM.GetMimeMessage(messageId)
        BZMessage = bz.BzMessage(messageBody)
        print(BZMessage.GetTickersFromMail())

    themessage = GM.GetMimeMessage(results['messages'][0]['id'])

    BenzingaMessage = bz.BzMessage(themessage)

    #soup = bs4.BeautifulSoup(themessage, features='html.parser')
    #paragraphs = soup.find_all('p')
    #for paragraph in paragraphs:
    #    print(paragraph.text)

    DB = DBConnect()


if __name__ == '__main__':
    main()
