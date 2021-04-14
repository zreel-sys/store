# Strings / localization file for greed
# Can be edited, but DON'T REMOVE THE REPLACEMENT FIELDS (words surrounded by {curly braces})

# Part of the translation by https://github.com/DarrenWestwood

# Currency symbol
currency_symbol = "R$"

# Positioning of the currency symbol
currency_format_string = "{symbol} {value}"

# Quantity of a product in stock
in_stock_format_string = "{quantity} disponivel"

# Copies of a product in cart
in_cart_format_string = "{quantity} na sacola"

# Product information
product_format_string = "<b>{name}</b>\n" \
                        "{description}\n" \
                        "{price}\n" \
                        "<b>{cart}</b>"

# Order number, displayed in the order info
order_number = "Pedido #{id}"

# Order info string, shown to the admins
order_format_string = "Usuario: {user}\n" \
                      "Data pedido: {date}\n" \
                      "\n" \
                      "{items}\n" \
                      "Valor total: <b>{value}</b>\n" \
                      "\n" \
                      "BIN: {notes}\n"

# Order info string, shown to the user
user_order_format_string = "{status_emoji} <b>Pedido {status_text}</b>\n" \
                           "{items}\n" \
                           "Valor total: <b>{value}</b>\n" \
                           "\n" \
                           "BIN: {notes}\n"

# Transaction page is loading
loading_transactions = "<i>Carregando transações...\n" \
                       "Espere alguns segundos.</i>"

# Transactions page
transactions_page = "Pagina <b>{page}</b>:\n" \
                    "\n" \
                    "{transactions}"

# transactions.csv caption
csv_caption = "A 📄 .csv file containing all transactions stored in the bot database was generated.\n" \
              "You can open this file with other programs, such as LibreOffice Calc, to process" \
              " the data."

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = "Seja bem-vindo a Lean Store!\n" \
                           "Material de qualidade!\n" \
                           "Leia ATENTAMENTE as INFORMAÇÕES antes de comprar!"

# Conversation: the start command was sent and the bot should welcome the user
conversation_after_start = " 🥤 Seja bem-vindo á Lean Store 🥤 \n" \
                           " 🚀 Material de qualidade 🚀 "
                           
# Conversation: to send an inline keyboard you need to send a message with it
conversation_open_user_menu = "O que deseja fazer?\n" \
                              "Você tem 💰<b>{credit}</b> de saldo.\n" \
                              "\n" \
                              "Para adicionar saldo e comprar CC's use o menu abaixo." 


# Conversation: like above, but for administrators
conversation_open_admin_menu = "Você é o 💼 <b>Gerente</b> dessa loja!\n" \
                               "O que quer fazer?" 

# Conversation: select a payment method
conversation_payment_method = "Qual método de pagamento deseja?"

# Conversation: select a product to edit
conversation_admin_select_product = "✏️ Qual produto você quer editar?"

# Conversation: select a product to delete
conversation_admin_select_product_to_delete = "❌ Qual produto gostaria de deletar?"

# Conversation: select a user to edit
conversation_admin_select_user = "Selecione um usuário"

# Conversation: click below to pay for the purchase
conversation_cart_actions = ""

# Conversation: confirm the cart contents
conversation_confirm_cart = "🛒 Produtos do seu carrinho:\n" \
                            "\n" \
                            "{product_list}" \
                            "Total: <b>{total_cost}</b>\n" \
                            "\n" \
                            "Confirme sua compra!" 
                         
# Conversation: the user activated the live orders mode
conversation_live_orders_start = "Pedidos em tempo real"
                                

# Conversation: help menu has been opened
conversation_open_help_menu = "What kind of help do you need?"

# Conversation: confirm promotion to admin
conversation_confirm_admin_promotion = "Tem certeza que deseja transformar esse usuário em 💼 ADMIN?\n" \
                                       "Essa ação é irreversível!"

# Conversation: language select menu header
conversation_language_select = "Escolha uma linguagem"

# Conversation: switching to user mode
conversation_switch_to_user_mode = " Ir para o modo 👤 Cliente.\n" \
                                   "Se quiser voltar para o menu de gerente digete /start"

# Notification: the conversation has expired
conversation_expired = "🕐  Faz tempo que não conversamos...bora comprar uma CC?\n" \
                       "Primeiro me atualize digitando /start "

# User menu: order
menu_order = "🛒 Comprar CC's"

# User menu: order status
menu_order_status = "🛍 Meus pedidos"

# User menu: add credit
menu_add_credit = "💵 Adicionar saldo"

# User menu: bot info
menu_bot_info = "ℹ️ Informações"

# User menu: cash
menu_cash = "💵 Pix"

# User menu: credit card
menu_credit_card = "💳 Cartão"

# Admin menu: products
menu_products = "📝️ Produtos"

# Admin menu: orders
menu_orders = "📦 Pedidos"

# Menu: transactions
menu_transactions = "💳 Lista de transações"

# Menu: edit credit
menu_edit_credit = "💰 Criar transação"

# Admin menu: go to user mode
menu_user_mode = "👤 Mudar para cliente"

# Admin menu: add product
menu_add_product = "✨ Novo produto"

# Admin menu: delete product
menu_delete_product = "❌ Deletar produto"

# Menu: cancel
menu_cancel = "🔙 Cancel"

# Menu: skip
menu_skip = "⏭ Pular"

# Menu: done
menu_done = "✅️ Confirmar"

# Menu: pay invoice
menu_pay = "💳 Pay"

# Menu: complete
menu_complete = "✅ Finalizado"

# Menu: refund
menu_refund = "✴️ Reembolso"

# Menu: stop
menu_stop = "🛑 Stop"

# Menu: add to cart
menu_add_to_cart = "➕ Adicionar"

# Menu: remove from cart
menu_remove_from_cart = "➖ Remover"

# Menu: help menu
menu_help = ""

# Menu: guide
menu_guide = "📖 Guide"

# Menu: next page
menu_next = "▶️ Next"

# Menu: previous page
menu_previous = "◀️ Previous"

# Menu: contact the shopkeeper
menu_contact_shopkeeper = "👨‍💼 Contact the store"

# Menu: generate transactions .csv file
menu_csv = "📄 .csv"

# Menu: edit admins list
menu_edit_admins = "🏵 Edit Managers"

# Menu: language
menu_language = ""

# Emoji: unprocessed order
emoji_not_processed = "*️⃣"

# Emoji: completed order
emoji_completed = "✅"

# Emoji: refunded order
emoji_refunded = "✴️"

# Emoji: yes
emoji_yes = "✅"

# Emoji: no
emoji_no = "🚫"

# Text: unprocessed order
text_not_processed = "pending"

# Text: completed order
text_completed = "completed"

# Text: refunded order
text_refunded = "refunded"

# Add product: name?
ask_product_name = "What should the product name be?"

# Add product: description?
ask_product_description = "What should the product description be?"

# Add product: price?
ask_product_price = "What should the product price be?\n" \
                    "Enter <code>X</code> if don't want the product to be for sale yet."

# Add product: image?
ask_product_image = "🖼 What image do you want the product to have?\n" \
                    "\n" \
                    "<i>Send the photo, or Skip this phase and don't add any image.</i>"

# Order product: notes?
ask_order_notes = "💳 Gostaria de escolher a BIN? *opcional\n" \
                  "\n" \
                  "✅ Caso queira escolher a BIN, digite abaixo.\n" \
                  "✅ Caso queira uma BIN aleatória, deixe em branco.\n" \
                  "\n" \
                  "<i>Se for mais que uma CC, digite as BINS seguidas de virgula.\n" \
                  "Exemplo: 438935, 504175, 636368, ETC... .</i>"

# Refund product: reason?
ask_refund_reason = " Digite o motivo do reembolso.\n" \
                    "👤 OBS: Aparecerá para o cliente."

# Edit credit: notes?
ask_transaction_notes = " Escreva a forma de pagamento que o cliente fez.\n" \
                        " Exemplo: Pix"

# Edit credit: amount?
ask_credit = "Quanto de saldo você gostária de adicionar?\n" \
             "\n" \
             "<i>Escreva abaixo:\n" \
             "Use o sinal </i><code>+</code><i> para adicionar saldo," \
             " e o sinal </i><code>-</code><i> para reduzir saldo (pouco usado).</i>"

# Header for the edit admin message
admin_properties = "<b>Permissions of {name}:</b>"

# Edit admin: can edit products?
prop_edit_products = "Edit products"

# Edit admin: can receive orders?
prop_receive_orders = "Receive orders"

# Edit admin: can create transactions?
prop_create_transactions = "Manage transactions"

# Edit admin: show on help message?
prop_display_on_help = "Show to customer"

# Thread has started downloading an image and might be unresponsive
downloading_image = "I'm downloading your photo!\n" \
                    "It might take a while... Please be patient!\n" \
                    "I won't be able to answer you while I'm downloading."

# Edit product: current value
edit_current_value = "The current value is:\n" \
                     "<pre>{value}</pre>\n" \
                     "\n" \
                     "<i>Press the Skip button below this message to keep the same value.</i>"

# Payment: cash payment info
payment_cash = "Para adicionar saldo a sua carteira envie um Pix para:.\n" \
               "2a408081-569f-4c97-b21d-a03a9072e9e4\n" \
               "Nome: Daniel - Banco: Inter\n" \
               "Após pagar, envie o comprovante e o número abaixo para @hazer171 ou @kingston171\n" \
               "<b>{user_cash_id}</b>"

# Payment: invoice amount
payment_cc_amount = "How many funds do you want to add to your wallet?\n" \
                    "\n" \
                    "<i>Select an amount with the buttons below, or enter it manually with the normal keyboard</i>"

# Payment: add funds invoice title
payment_invoice_title = "Adicionar saldo"

# Payment: add funds invoice description
payment_invoice_description = "Paying this invoice will add {amount} to your wallet."

# Payment: label of the labeled price on the invoice
payment_invoice_label = "Reload"

# Payment: label of the labeled price on the invoice
payment_invoice_fee_label = "Transaction fee"

# Notification: order has been placed
notification_order_placed = "A new order was placed:\n" \
                            "{order}"

# Notification: order has been completed
notification_order_completed = "Sua compra foi fechada!\n" \
                               "{order}"

# Notification: order has been refunded
notification_order_refunded = "Sua compra foi reembolsada!\n" \
                              "{order}"

# Notification: a manual transaction was applied
notification_transaction_created = "ℹ️  A new transaction has been applied to your wallet:\n" \
                                   "{transaction}"

# Refund reason
refund_reason = "Refund reason:\n" \
                "{reason}"

# Info: informazioni sul bot
bot_info = 'This bot is using <a href="https://github.com/Steffo99/greed">greed</a>,' \
           ' a framework by @Steffo for Telegram payments released under the' \
           ' <a href="https://github.com/Steffo99/greed/blob/master/LICENSE.txt">' \
           'Affero General Public License 3.0</a>.\n'

# Help: guide
help_msg = "greed's guide is available at this address:\n" \
           "https://docs.google.com/document/d/1f4MKVr0B7RSQfWTSa_6ZO0LM4nPpky_GX_qdls3EHtQ/"

# Help: contact shopkeeper
contact_shopkeeper = "Currently, the staff available to provide user assistance is composed of:\n" \
                     "{shopkeepers}\n" \
                     "<i>Click / Tap one of their names to contact them in a Telegram chat.</i>"

# Success: product has been added/edited to the database
success_product_edited = "✅ The product has been successfully added/modified!"

# Success: product has been added/edited to the database
success_product_deleted = "✅ The product has been successfully deleted!"

# Success: order has been created
success_order_created = "✅ The order was sent successfully!\n" \
                        "\n" \
                        "{order}"

# Success: order was marked as completed
success_order_completed = "✅ You marked the order #{order_id} as completed."

# Success: order was refunded successfully
success_order_refunded = "✴️ Order #{order_id} was refunded."

# Success: transaction was created successfully
success_transaction_created = "✅ The transaction was successfully created!\n" \
                              "{transaction}"

# Error: message received not in a private chat
error_nonprivate_chat = "⚠️ This bot only works in private chats."

# Error: a message was sent in a chat, but no worker exists for that chat.
# Suggest the creation of a new worker with /start
error_no_worker_for_chat = "⚠️ The conversation with the bot was interrupted.\n" \
                           "To restart it, send the /start command to the bot."

# Error: add funds amount over max
error_payment_amount_over_max = "⚠️ The maximum amount that can be added in a single transaction is {max_amount}."

# Error: add funds amount under min
error_payment_amount_under_min = "⚠️ The minimum amount that can be added in a single transaction is {min_amount}."

# Error: the invoice has expired and can't be paid
error_invoice_expired = "⚠️ This invoice has expired and was canceled. If you still want to add funds, use the Add" \
                        " funds menu option."

# Error: a product with that name already exists
error_duplicate_name = "️⚠️ Já existe um produto com esse nome."

# Error: not enough credit to order
error_not_enough_credit = "⚠️ You do not have enough credit to place the order."

# Error: order has already been cleared
error_order_already_cleared = "⚠️  This order has already been processed."

# Error: no orders have been placed, so none can be shown
error_no_orders = "⚠️  You haven't placed any order yet, so there is nothing to display."

# Error: selected user does not exist
error_user_does_not_exist = "⚠️  The selected user does not exist."

# Fatal: conversation raised an exception
fatal_conversation_exception = "☢️ Oh no! An <b>error</b> interrupted this conversation\n" \
                               "The error was reported to the bot owner so that he can fix it.\n" \
                               "To restart the conversation, send the /start command again."
