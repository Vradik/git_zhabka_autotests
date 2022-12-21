from appium import webdriver
from selenium.webdriver.common.by import By



class Locators (object):
    def __init__(self, driver: webdriver.Remote):

        self.driver = driver


# Field for entering a mobile phone number
    @property
    def input_phone(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/editPhone')

# Welcome text on the start screen
    @property
    def text_greeting(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/greeting')

# Phone confirmation button
    @property
    def confirmation_phone_numb(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/lets_start_button')

# SMS code input field
    @property
    def code_sms(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/codeSmsPinView')

# location check on the PIN code input screen (1 time)
    @property
    def code_pin_1_screen(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/textStepFirst')

# location check on the PIN code input screen (2 time)
    @property
    def code_pin_2_screen(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/textStepSecond')

# Pin code input field
    @property
    def code_pin(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/codePasswordView')

# checking the location of the Frog Learner on the screen
    @property
    def chat_screen(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/chat_title')

# Skip training (skip chat)
    @property
    def skip_chat(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/navigationIcon')

# home screen location check
    @property
    def main_screen(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/tvCardTitle')

# Billing button (on each screen, in the center, at the top)
    @property
    def billing_button(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/iconQrBilling')

# Open the chart screen
    @property
    def chart(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/iconDiagram')

# Change icon mode after billing (QR code, nfs)
    @property
    def change_mode_icon(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/change_mode_icon')

# The button to distribute the link of the issued invoice (on the screen immediately after issuing the invoice)
    @property
    def share(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/icon_share')

# Return to the main screen from the newly issued invoice screen
    @property
    def back_to_main(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/ivBack')

# Change the payment destination
    @property
    def icon_purpose(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/icon_purpose')

# Entering the name of the new business
    @property
    def org_name(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/org_name')

# Entering the name of the outlet
    @property
    def outlet_name(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/outlet_name')

# Entering the value of the IBAN code
    @property
    def iban(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/iban')

# Entering the payment destination (on the new business registration screen)
    @property
    def org_purpose(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/purpose')

# Save new business button
    @property
    def org_save_button(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/save_button')

# Issued invoice screen: Help button
    @property
    def help_button(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/llHelpButton')

# Issued invoice screen: transaction number
    @property
    def transaction_number(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/tvTransactionNumber')

# Issued account screen: the time of issue (formation) of the account
    @property
    def time_transaction(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/tvTransactionEmitted')

# Issued invoice screen: cancel invoice
    @property
    def cancel_transaction(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/llCancelPaymentButton')

# Issued invoice screen: pop-up window - yes
    @property
    def popup_yes_button(self):
        return self.driver.find_element(By.ID, 'android:id/button1')

# Issued invoice screen: pop-up window - no
    @property
    def popup_no_button(self):
        return self.driver.find_element(By.ID, 'android:id/button2')

# Issued invoice screen: renew the invoice
    @property
    def restart_transaction(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/llRestartPaymentButton')

# Issued invoice screen: delete invoice
    @property
    def delete_transaction(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/llDeletePaymentButton')

# Issued invoice screen: the second tab (photo, docs) - the name of the transaction
    @property
    def name_transaction(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/etName')

# Issued invoice screen: the second tab (photo, docs) - confirm the title
    @property
    def confirm_name_transaction(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/ivNameConfirm')

# Issued invoice screen: the second tab (photo, docs) - cancel the name
    @property
    def cancel_name_transaction(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/ivNameCancel')

# Issued invoice screen: the second tab (photo, docs) - download Documents
    @property
    def upload_file(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/bUploadFile')

# Issued invoice screen: the second tab (photo, docs) - download the image
    @property
    def upload_image(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/bUploadPic')

# Issued invoice screen: Group Payment Button
    @property
    def start_group_payment(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/llGroupPaymentButton')

# Group payments: Group Payment Button from the list transactions
    @property
    def start_group_payment_from_list(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/textPayerName')

# Group payments: group name
    @property
    def title_group_payment(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/etTitle')

# Group payments: start a group payment
    @property
    def start_group_payment2(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/bBegin')

# Group payments: set up a group payment
    @property
    def settings_group_payment(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/ivSettings')

# Group payments: complete a group payment
    @property
    def finish_group_payment(self):
        return self.driver.find_element(By.ID, 'ua4ek.board:id/bFinish')
