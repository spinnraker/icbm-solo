    const mysql = require("mysql2/promise");

    mysql.createConnection = async function (param) {
        
    }
    const selectAllDb = async permissionDesc => {
        const connection = await mysql.createConnection({
            host: "sql5.freesqldatabase.com",
            user: "sql5439306",
            password: "r66RVvxnKM",
            database: "sql5439306",
            port: 3306,
        });

        try {
            await connection.query('Select * From Customer;');

            console.log("Called");
        } catch (e) {
            console.log(e);
        }
    };

    function setup() {
        createCanvas(1000,1000);

        var button = select('#submit');
        button.mousePressed(query);
    }

    function query() {
        var url = connection.query("SELECT * FROM Customer;");
    }

    query();
    setup();
    selectAllDb().then(r => {});