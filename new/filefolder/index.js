const express = require("express");
const app = express();
const mongoose = require("mongoose");
const dotenv = require("dotenv");
const bodyparser = require("body-parser")


dotenv.config();
const employe = require("./routes/user");
const auth = require("./routes/auth");
const company = require("./routes/company");


mongoose
    .connect(process.env.URL)
    .then(() => console.log("DB Connection Successfull!"))
    .catch((err) => {
        console.log(err);
    });

app.use(bodyparser.json());
app.use(bodyparser.urlencoded({ extended: true }))
app.use("/api/auth", auth);
app.use("/api/users", employe);
app.use("/api/company", company);





app.listen(3000, () => { console.log("server is running") })