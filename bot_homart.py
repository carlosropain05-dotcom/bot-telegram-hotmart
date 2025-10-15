from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

TOKEN = "7325685200:AAFkvUYw9fN444IWCjPi3KSGAjLEKd0zteU"

# Link correcto de Hotmart con redirección
HOTMART_LINK = "https://go.hotmart.com/M102398854K?redirectionUrl=https%3A%2F%2Facademiadigitaldye.com%2Faccesorios-de-resina-para-emprender%2F"

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎨 Ver Curso de Resina", callback_data='curso')],
        [InlineKeyboardButton("ℹ️ Más Información", callback_data='info')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 ¡Hola! Soy el asistente de Carlos.\n\n"
        "Te ayudaré a conocer el curso de accesorios en resina 🔥\n\n"
        "👇 Elige una opción:",
        reply_markup=reply_markup
    )

# Manejar botones
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'curso':
        keyboard = [[InlineKeyboardButton("🛒 Acceder al Curso", url=HOTMART_LINK)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.reply_text(
            "🎨 *Curso: Accesorios en Resina para Emprender*\n\n"
            "✨ Aprende a crear hermosos accesorios y emprende.\n\n"
            "📚 *Incluye:*\n"
            "• Técnicas profesionales\n"
            "• Materiales necesarios\n"
            "• Diseños únicos\n"
            "• Estrategias de venta\n\n"
            "💰 *Oferta especial:* -50% HOY\n"
            "💳 Pago único, sin mensualidades\n"
            "✅ Certificado incluido\n"
            "🎁 +11 horas de contenido\n\n"
            "👇 Haz clic para ver detalles:",
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
    
    elif query.data == 'info':
        keyboard = [
            [InlineKeyboardButton("🛒 Comprar Ahora", url=HOTMART_LINK)],
            [InlineKeyboardButton("« Volver", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.reply_text(
            "📋 *Información del Curso*\n\n"
            "✅ Acceso inmediato y de por vida\n"
            "✅ Certificado incluido\n"
            "✅ Actualizaciones gratis\n"
            "✅ Garantía de 7 días\n"
            "✅ Material descargable\n"
            "✅ Comunidad VIP WhatsApp\n"
            "✅ +60 clases paso a paso\n\n"
            "🚀 ¡Comienza hoy con 50% OFF!",
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
    
    elif query.data == 'menu':
        keyboard = [
            [InlineKeyboardButton("🎨 Ver Curso de Resina", callback_data='curso')],
            [InlineKeyboardButton("ℹ️ Más Información", callback_data='info')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.reply_text(
            "🏠 *Menú Principal*\n\n"
            "Elige una opción:",
            parse_mode='Markdown',
            reply_markup=reply_markup
        )

# Manejar mensajes de texto
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "curso" in text or "resina" in text or "precio" in text or "comprar" in text:
        keyboard = [[InlineKeyboardButton("🛒 Ver Curso", url=HOTMART_LINK)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "🎨 ¡Aquí está el curso de resina!\n\n"
            "💰 Hoy con 50% de descuento 🔥",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            "Escribe 'curso' para ver el producto 😊\n"
            "O usa /start para ver el menú principal"
        )

# Función principal
def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))
    
    print("🤖 Bot iniciado correctamente")
    print("📱 Prueba enviando /start a tu bot")
    
    app.run_polling()

if __name__ == '__main__':
    main()