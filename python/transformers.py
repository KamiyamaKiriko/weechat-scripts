# -*- encoding: utf-8 -*-
import weechat
import re
stripFormatting = re.compile(r"|\d{0,2}(,\d{0,2})?")

script = {
    "name": "transformers",
    "author": "KamiyamaKiriko",
    "version": "0.2",
    "license": "MIT",
    "description": "Fancily fancify your fancy messages",
}

replacements = {
    ":V": u"<̈",
    "<3": u"4<3 ",

    "qUcyy": u"┐(￣ー￣)┌",
    "miyabi.png": u"( ¬‿¬)",
    ";we:": u"┐('～`；)┌",
    ";dohoho:": u"( ￣ ▽ ￣ )ノ Ｄｏｈｏｈｏｈｏｈｏ～",
    ";uh:": u"( ﾟ‿ ﾟ)",
    ";rage:": u"(╬ ಠ益ಠ)",
    ";obto:": u"ヾ(๑╹◡╹๑)ノ",
    ";kyubey:": u"／人◕ ‿‿ ◕人＼",
    ";cryingdisapprove:": u"ಥ_ಥ",
    ";disapprove:": u"ಠ_ಠ",
    ";cries:": u"11｡･ﾟ･(ﾉД`)11･ﾟ･｡ ",
    ";donger:": u"ヽ༼ຈلຈ༽ﾉ",
}


def hook_message_send(data, buffer, command):
    text = weechat.buffer_get_string(buffer, 'input').decode("utf-8")
    if text.startswith('/') and not text.startswith('//'):
        return weechat.WEECHAT_RC_OK

    for original in replacements:
        text = text.replace(original, replacements[original])

    if text.startswith(">"):
        text = u"3"+text

    if weechat.buffer_get_string(buffer, "name").startswith("bitlbee"):
        text = stripFormatting.sub("", text)

    weechat.buffer_set(buffer, 'input', text.encode("utf-8"))
    return weechat.WEECHAT_RC_OK


weechat.register(script['name'], script['author'], script['version'], script['license'], script['description'], "", "")
weechat.hook_command_run("/input return", "hook_message_send", "")
