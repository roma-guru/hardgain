# Generated by Django 2.0 on 2018-01-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0003_auto_20180108_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainday',
            name='mood',
            field=models.CharField(help_text='😀 😁 😂 😃 😄 😅 😆 😇 😈 😉 😊 😋 😌 😍 😎 😏 😐 😑 \n😒 😓 😔 😕 😖 😗 😘 😙 😚 😛 😜 😝 😞 😟 😠 😡 😢 😣 😤 😥 😦 \n😧 😨 😩 😪 😫 😬 😭 😮 😯 😰 😱 😲 😳 😴 😵 😶 😷 🙁 🙂 🙃 🙄 \n    ', max_length=5),
        ),
    ]
