class CreateAccount{
    enterURL(){
        cy.visit('https://magento.softwaretestingboard.com/')

    }
    clickOnCreatAccount(){
        cy.xpath("//span[contains(text(),'Create an Account')]").click()

    }
    enterFirstName(value){
        cy.xpath("//input[@id='firstname']").type(value).click()

    }
    enterLastName(value){
        cy.xpath("//input[@id='lastname']").type(value).click()

    }
    clickOnCreatAccountButton(){
        cy.xpath("//span[contains(text(),'Create an Account')]").click()

    }
    verifySuccesmessage(){
        cy.xpath("//div[@data-ui-id='message-success']").should("have.text","Thank you for registering with Main Website Store")

    }
    enterUsername(){
        cy.xpath("//input[@id='email_address']").type(value).click()

    }
    enterPassword(value){
        cy.xpath("//input[@id='password']").type(value).click()

    }
    enterConfirmPassword(value){
        cy.xpath("//input[@id='password-confirmation']").type(value).click()

    }
    clickOnSigninButton(){
        cy.xpath("//span[contains(text(),'Sign In')]").click()

    }
    

}
export default  CreateAccount