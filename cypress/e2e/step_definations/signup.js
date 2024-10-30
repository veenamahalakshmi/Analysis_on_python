///<reference types="cypress"  />


import { Given , When ,Then ,And} from "cypress-cucumber-preprocessor/steps";
import createaccount from "../Page_Objects/signup.po"


const createacc = new createaccount()

var valuedata;

beforeEach(()=>{
 cypress.fixture('signup_inputs.json').then(function (value) {
    valuedata=value

 })
})

Given ("Launch the URL",()=>{
    createacc.enterURL()

})
And ("click on CreateAccount",()=>{
    createacc.clickOnCreatAccount()

})
When ("user Fills all the mandatory fields", function(){
    createacc.enterFirstName(valuedata.Firstname)
    createacc.enterLastName(valuedata.Lastname)
    createacc.enterUsername(valuedata.Email)
    createacc.enterPassword(valuedata.password)
    createacc.enterConfirmPassword(valuedata.confirmpassword)
})

And ("click on CreateAccount button",()=>{
    createacc.clickOnCreatAccountButton()

})
Then ("Verify the success message",()=>{
    createacc.verifySuccesmessage()

})

Then ("Enter username and password",function(){
    createacc.enterUsername(valuedata.Email)
    createacc.enterPassword(valuedata.password)

})
And ( "click on signin button ",()=>{
    createacc.clickOnSigninButton()


})
And  ("verify application should get open",()=>{
    createacc.verifyapp()

})