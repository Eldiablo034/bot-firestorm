import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Inserisci qui il token ricevuto da @BotFather
TOKEN = "IL_TUO_TOKEN_QUI"

# Configura i log per vedere eventuali errori nel terminale
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Funzione che gestisce i messaggi ricevuti
async def gestisci_messaggi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ignora aggiornamenti che non contengono testo (es. foto, adesivi, cambi di stato)
    if not update.message or not update.message.text:
        return

    testo_ricevuto = update.message.text.lower()
    tipo_chat = update.message.chat.type

    # Verifica che il messaggio provenga da un gruppo o supergruppo
    if tipo_chat in ["group", "supergroup"]:
        
        # Logica di risposta (personalizzabile a piacimento)
        if "ciao bot" in testo_ricevuto:
            nome_utente = update.message.from_user.first_name
            await update.message.reply_text(f"Ciao {nome_utente}! Come posso aiutarti?")
            
        elif "regole" in testo_ricevuto:
            await update.message.reply_text("📜 Ecco le regole del gruppo: sii gentile e niente spam!")

def main():
    # Inizializza l'applicazione con il tuo Token
    app = Application.builder().token(TOKEN).build()

    # Aggiunge un gestore per tutti i messaggi di testo (esclusi i comandi con /)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gestisci_messaggi))

    print("Bot avviato e in ascolto nei gruppi...")
    # Avvia il bot in modalità polling (controlla continuamente nuovi messaggi)
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
