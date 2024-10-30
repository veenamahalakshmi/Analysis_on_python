const { defineConfig } = require("cypress");
const cucumber = require ("cypress-cucumber-preprocessor").default

module.exports = defineConfig({
  e2e: {
    specPattern:"cypress/e2e/**/*.{feature,features}",
    setupNodeEvents(on, config) {
      on("file:preprocessor",cucumber())
     
      // implemnt node event listeners here
    },
  },
});
