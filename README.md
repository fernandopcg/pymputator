pymputator
=========

 
Pymputator solves what hundreds of Logicalis Spain employees suffer every day: Checking in their work hours in an obsolete, slow, non-standars-compliant and inefficient website.

Now you can be pympin' in no time, and quickly get back to work without fear of those warning e-mails every single week


Version
----

0.1b

Installation
----


#### config.json:

Edit your username and password
```
{
	"user": "YOUR_USERNAME_HERE",
	"pass": "YOUR_PASSWORD_HERE"
}
```
#### pympute.py
Edit month and non-working dates (Such as local holidays) list inside the script as appropriate:

```
MONTH = pd.date_range('2014-11-01', '2014-11-30', freq='D')
NOT_WORKING_DAYS = [datetime(2014, 11, 1)]
```






Props
-----------

Pymputator uses a number of open source projects to work properly:

* [Pandas] - Python Data Analysis Library, providing high-performance, easy-to-use data structures and data analysis tools
* [Requests] - An Apache2 Licensed HTTP library, written in Python, for human beings

Installation
--------------

1- Get your copy
```
git clone git://github.com/fernandopcg/pymputator.git
```

2- Configure files as stated above and then launch the script
```sh
python pymputator.py
```

3- ???

4- Profit

Disclaimer and licensing
----

This software is under [MIT License]


**Free Software, Hell Yeah!**

[Pandas]:http://daringfireball.net/
[Requests]:http://twitter.com/thomasfuchs
[MIT License]:http://opensource.org/licenses/MIT
