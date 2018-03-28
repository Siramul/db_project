create table User(user_id serial primary key, first_name varChar(10), last_name varChar(10),e_mail varChar(20),phone_number varChar(10), password varChar(10),user_name varChar(10));

create table Chat(chat_id serial primary key, chat_name varChar(10),manager integer references User(user_id));

create table Message(message_id serial primary key,sender integer references User(user_id), content varChar(200),reply_id integer references Message(mesage_id),time_stamp timestamp());

create table Member(user_id integer references User(user_id),chat_id integer references Chat(chat_id),primary key (user_id,chat_id));

create table Contact(user_id integer references User(user_id),contact_id integer references User(user_id),primary key (user_is,contact_id));

create table Like_Dislike(user_id integer references User(user_id),message_id integer references Message (message_id),like_dislike boolean , primary key (user_id, message_id));

create table Reply (user_id integer references User(user_id),message_id integer references Message(message_id),primary key (user_id,message_id));

create table Contains(chat_id integer references Chat(chat_id),message_id integer references Message (message_id),primary key (chat_id,message_id));

