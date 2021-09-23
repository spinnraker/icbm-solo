    const mysql = require("mysql2/promise");

    const insertIntoDB = async () => {
        const connection = await mysql.createConnection({
            host: "sql5.freesqldatabase.com",
            user: "sql5439306",
            password: "r66RVvxnKM",
            database: "sql5439306",
            port: 3306,
        });

        try {
            await connection.query(
                "INSERT INTO Customer (Customer_Id, Customer_Gender, Customer_Name, Customer_Fname, Customer_Lname, Customer_Email,Customer_TotalFinances,Customer_Bdate,Customer_Risk) VALUES ('1', 'Male', 'Bryan Clark', 'Bryan', 'Clark', 'urmom@msn.com', '103.85', '20210922 10:30:00 PM', '1')"
            );

            console.log("Inserted");
        } catch (e) {
            console.log(e);
        }
    };

    insertIntoDB();
