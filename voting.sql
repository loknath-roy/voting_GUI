create database voting;
use voting;
create table registration
(
First_name varchar(50),
Last_name varchar(50),
Email_Id varchar(50),
Password varchar(50),
Confirm_pass varchar(50),
Aadhaar_no varchar(20),
DOB varchar(20),
Gender varchar(50);
)
alter table registration
add Status varchar(50);
alter table registration
add party varchar(50);


select * from registration;
create table admin_details
(
id varchar(50),
pass varchar(50)
);
insert into admin_details(id , pass) values("LoknathRoy", "Lok@1997");
select * from admin_details; 