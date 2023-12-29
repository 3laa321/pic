
from botAssest import *

#-----------------text----------------

@bot.message_handler(commands=['blur'])
def send_start(message):
    path_us = str(message.from_user.id)


    with open( 'user_data/'+path_us , 'w+' ) as f:
       lines = f.readlines()
       lines.sort()
       jj = str(lines).replace('[','').replace(']','').replace('\'','').replace('\"','')


       if jj == 'en' :
        messa = en_wating
        default_caption = en_caption
        up_100 = en_up_100
        caption_cus1 =en_caption_cus1
        caption_cus2 =en_caption_cus2

       if jj == 'ar' :
        messa = ar_wating
        default_caption = ar_caption
        up_100 = ar_up_100
        caption_cus1 =ar_caption_cus1
        caption_cus2 =ar_caption_cus2


       if jj == 'ru' :
        messa = ru_wating
        default_caption = ru_caption
        up_100 = ru_up_100
        caption_cus1 =ru_caption_cus1
        caption_cus2 =ru_caption_cus2

       else :
        outfile = open( 'user_data/'+ path_us, 'w')
        outfile.write( 'en' )
        messa = en_wating
        default_caption = en_caption
        up_100 = en_up_100
        caption_cus1 =en_caption_cus1
        caption_cus2 =en_caption_cus2

# ----------------Blur----------------


    cmd_text = message.text
    file_name = ''.join((random.choice(string.ascii_lowercase)for x in range(10)))

    file_info = bot.get_file(message.reply_to_message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("Editing/" + file_name + '.png', 'wb') as new_file:
        new_file.write(downloaded_file)

    if cmd_text == "/blur":

        bot.reply_to(message, text=messa, parse_mode='html')

        Photo = Image.open("./Editing/" + file_name + ".png")
        photo = Photo.filter(ImageFilter.GaussianBlur(radius=10))
        photo.save("./Editing/" + file_name + ".png")
        bot.send_photo(chat_id=message.from_user.id, photo=open("./Editing/" + file_name + ".png", 'rb'), caption=default_caption, parse_mode="html")

    else:

        str1 = message.text
        res = [int(i) for i in str1.split() if i.isdigit()]
        blur_radious_num = str(res).replace('[','').replace(']','').replace('\'','').replace('\"','')
        blur_radious = int(float(blur_radious_num))



        if blur_radious < 101:


            bot.reply_to(message, text=messa, parse_mode='html')

            Photo = Image.open("./Editing/" + file_name + ".png")
            photo = Photo.filter(ImageFilter.GaussianBlur(radius=blur_radious))
            photo.save("./Editing/" + file_name + ".png")
            captionnn = caption_cus1  + blur_radious_num + caption_cus2
            bot.send_photo(chat_id=message.from_user.id, photo=open("./Editing/" + file_name + ".png", 'rb'),caption=captionnn , parse_mode='html' )

        else:
            bot.reply_to(message, text=up_100, parse_mode='markdown')
