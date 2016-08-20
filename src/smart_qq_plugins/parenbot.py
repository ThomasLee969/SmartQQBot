# -*- coding: utf-8 -*-
import random

from smart_qq_bot.logger import logger
from smart_qq_bot.signals import (
    on_all_message,
    on_group_message,
    on_private_message,
    on_discuss_message,
)

PARENS = {
    '<': '>',  # Not working now.
    '(': ')',
    '[': ']',
    '{': '}',
    '（': '）',
    '［': '］',
    '｛': '｝',
    '⦅': '⦆',
    '〚': '〛',
    '⦃': '⦄',
    '“': '”',
    '‘': '’',
    '‹': '›',
    '«': '»',
    '「': '」',
    '〈': '〉',
    '《': '》',
    '【': '】',
    '〔': '〕',
    '⦗': '⦘',
    '『': '』',
    '〖': '〗',
    '〘': '〙',
    '｢': '｣',
    '⟦': '⟧',
    '⟨': '⟩',
    '⟪': '⟫',
    '⟮': '⟯',
    '⟬': '⟭',
    '⌈': '⌉',
    '⌊': '⌋',
    '⦇': '⦈',
    '⦉': '⦊',
    '❛': '❜',
    '❝': '❞',
    '❨': '❩',
    '❪': '❫',
    '❴': '❵',
    '❬': '❭',
    '❮': '❯',
    '❰': '❱',
    '❲': '❳',
    '⏜': '⏝',
    '⎴': '⎵',
    '⏞': '⏟',
    '〝': '〞',
    '︵': '︶',
    '⏠': '⏡',
    '﹁': '﹂',
    '﹃': '﹄',
    '︹': '︺',
    '︻': '︼',
    '︗': '︘',
    '︿': '﹀',
    '︽': '︾',
    '﹇': '﹈',
    '︷': '︸',
    '〈': '〉',
    '⦑': '⦒',
    '⧼': '⧽',
    '﹙': '﹚',
    '﹛': '﹜',
    '﹝': '﹞',
    '⁽': '⁾',
    '₍': '₎',
    '⦋': '⦌',
    '⦍': '⦎',
    '⦏': '⦐',
    '⁅': '⁆',
    '⸢': '⸣',
    '⸤': '⸥',
    '⟅': '⟆',
    '⦓': '⦔',
    '⦕': '⦖',
    '⸦': '⸧',
    '⸨': '⸩',
    '｟': '｠',
    '⧘': '⧙',
    '⧚': '⧛',
    '⸜': '⸝',
    '⸌': '⸍',
    '⸂': '⸃',
    '⸄': '⸅',
    '⸉': '⸊',
    '᚛': '᚜',
    '༺': '༻',
    '༼': '༽',
}

GROUP_NAME = '清'

@on_group_message(name='fix')
def fix(msg, bot):
    if msg.src_group_name == GROUP_NAME:
        reply = bot.reply_msg(msg, return_function=True)

        logger.info('[%s] @%s: %s', msg.src_group_name, msg.src_sender_card, content)

        stack = []
        bads = ''

        for ch in content:
            if ch in PARENS:
                stack.append(ch)
            elif ch in PARENS.values():
                if len(stack) == 0 or ch != PARENS[stack[-1]]:
                    bads += ch
                else:
                    stack.pop()

        close = ''
        for ch in reversed(stack):
            close += PARENS[ch]


        r = ''
        if len(close) > 0:
            r += close + ' ○(￣□￣○)'
        if len(bads) > 0:
            if len(r) > 0:
                r += ' '
            r += '(╯°□°）╯ ' + bads

        if len(r) > 0:
            r = '@{} {}'.format(msg.src_sender_card, r)
            logger.info('[%s] me: %s', msg.src_group_name, r)
            reply(r)
