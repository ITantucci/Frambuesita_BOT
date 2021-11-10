from  CoinmarketcapAPI import * 
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def start(update, context):

    update.message.reply_text('Total: $' + str(Total()))

    update.message.reply_text('BTC: $' + str(Set_BTC_Value()) + '\nCurrent: $' + str(MioBTC()))
   
    update.message.reply_text('ETH: $' + str(Set_ETH_Value()) + '\nCurrent: $' + str(MioETH()))

    update.message.reply_text('BNB: $' + str(Set_BNB_Value()) + '\nCurrent: $' + str(MioBNB()))
   
    update.message.reply_text('ADA: $' + str(Set_ADA_Value()) + '\nCurrent: $' + str(MioADA()))
   
    update.message.reply_text('SHIB: $' + str(Set_SHIB_Value()) + '\nCurrent: $' + str(MioSHIB()))
  
    update.message.reply_text('SLP: $' + str(Set_SLP_Value()) + '\nCurrent: $' + str(MioSLP()))
  
    update.message.reply_text('XRP: $' + str(Set_XRP_Value()) + '\nCurrent: $' + str(MioXRP()))
  
    update.message.reply_text('LINK: $' + str(Set_LINK_Value()) + '\nCurrent: $' + str(MioLINK()))
  
    update.message.reply_text('ATOM: $' + str(Set_ATOM_Value()) + '\nCurrent: $' + str(MioATOM()))
   
    update.message.reply_text('DOGE: $' + str(Set_DOGE_Value()) + '\nCurrent: $' + str(MioDOGE()))
   
    update.message.reply_text('PVU: $' + str(Set_PVU_Value()) + '\nCurrent: $' + str(MioPVU()))


def main():
    updater = Updater("Telegram Bot API Here", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("Start", start))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
