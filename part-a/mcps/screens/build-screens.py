# -*- coding: utf-8 -*-
# Desktop mockups for section 5.4. All data is invented (marked "נתוני דמה").
from html import escape as E

TPI_MENU = ['ייבוא קובץ', 'הרצת בדיקה', 'חריגות', 'חריגות לפי ותק', 'כמות צפויה', 'תיק פק"ע',
            'דיווחים מתוקנים', 'מכשירים ועובדים', 'ספי חריגה']
MGR_MENU = ['תיק פק"ע', 'תיק עובד', 'חריגות לפי ותק', 'דוח לפי גידול', 'דוח לפי פעולה ושלב', 'משתמשים']
TPI_USER = 'נטלי · אחראית תפ"י'
MGR_USER = 'דותן · מנהל תפעול וייצור · מנהל מערכת'

CSS = """
*{box-sizing:border-box} body{margin:0;font-family:'Liberation Sans','DejaVu Sans',sans-serif;font-size:14px;color:#1d2a24;background:#c9d1cc}
.win{width:1280px;height:800px;margin:0;background:#f4f6f5;display:flex;flex-direction:column;direction:rtl;border:1px solid #6d7a73}
.title{height:40px;background:#2f5d46;color:#fff;display:flex;align-items:center;padding:0 14px;justify-content:space-between}
.title b{font-size:15px} .wbtn{display:flex;gap:8px;direction:ltr} .wbtn span{width:12px;height:12px;border-radius:50%;background:#dfe7e2;display:inline-block}
.body{flex:1;display:flex;min-height:0}
.side{width:200px;background:#e3ebe6;border-left:1px solid #c3cfc8;padding:12px 0}
.side div{padding:9px 18px;color:#2e3d35} .side .on{background:#2f5d46;color:#fff;font-weight:bold}
.main{flex:1;padding:16px 22px;overflow:hidden;position:relative}
h1{font-size:20px;margin:0 0 4px} .sub{color:#5b6a62;margin-bottom:12px}
.bar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;background:#fff;border:1px solid #cfd8d3;padding:10px 12px;border-radius:6px;margin-bottom:12px}
.f{display:flex;flex-direction:column;gap:3px;font-size:12px;color:#4b5a52}
.in{background:#fff;border:1px solid #9fb0a7;border-radius:4px;padding:5px 8px;min-width:110px;font-size:13px;color:#1d2a24}
.in.err{border:2px solid #b3261e}
.btn{background:#2f5d46;color:#fff;border-radius:4px;padding:7px 14px;font-weight:bold;font-size:13px;display:inline-block}
.btn.sec{background:#fff;color:#2f5d46;border:1px solid #2f5d46} .btn.warn{background:#8a5a00}
.cards{display:flex;gap:10px;margin-bottom:12px} .card{flex:1;background:#fff;border:1px solid #cfd8d3;border-radius:6px;padding:10px 12px}
.card .n{font-size:24px;font-weight:bold;color:#2f5d46} .card .l{color:#5b6a62;font-size:12px}
.card.bad .n{color:#b3261e} .card.amb .n{color:#8a5a00}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #cfd8d3;font-size:13px}
th{background:#dfe8e3;text-align:right;padding:6px 8px;font-size:12px;color:#33443b;border-bottom:1px solid #c3cfc8}
td{padding:6px 8px;border-bottom:1px solid #e6ebe8} tr.sel td{background:#e8f1ec} tr.hl td{background:#fdf1e0}
.tag{display:inline-block;padding:1px 7px;border-radius:9px;font-size:11px;font-weight:bold}
.open{background:#fbe3e1;color:#9b1c14} .fixed{background:#dff0e4;color:#1f6b3a} .negl{background:#e9e9e9;color:#555}
.ver{background:#e4e9f7;color:#2b4a9b} .warnt{background:#fdf1e0;color:#8a5a00}
.panel{background:#fff;border:1px solid #cfd8d3;border-radius:6px;padding:12px;margin-top:12px}
.panel h3{margin:0 0 8px;font-size:15px}
.cols{display:flex;gap:12px} .cols>div{flex:1}
.chg{background:#fdf1e0;font-weight:bold}
.status{height:24px;background:#dfe7e2;border-top:1px solid #c3cfc8;font-size:11px;color:#4b5a52;display:flex;align-items:center;padding:0 12px;justify-content:space-between}
.overlay{position:absolute;inset:0;background:rgba(20,30,25,.45);display:flex;align-items:center;justify-content:center}
.modal{width:520px;background:#fff;border-radius:8px;padding:18px 20px;box-shadow:0 8px 30px rgba(0,0,0,.35)}
.modal h3{margin:0 0 10px;font-size:17px}
.ta{border:1px solid #9fb0a7;border-radius:4px;height:70px;padding:6px 8px;color:#1d2a24}
.banner{background:#fdf1e0;border:1px solid #e0b46a;color:#6b4500;border-radius:6px;padding:8px 12px;margin-bottom:12px;font-weight:bold}
.note{font-size:12px;color:#5b6a62;margin-top:6px} .red{color:#b3261e;font-weight:bold} .muted{color:#7a8780}
.chk{display:inline-block;width:13px;height:13px;border:1px solid #6d7a73;border-radius:2px;vertical-align:middle;background:#fff}
.chk.on{background:#2f5d46;border-color:#2f5d46}
.radio{display:inline-block;width:12px;height:12px;border:1px solid #6d7a73;border-radius:50%;vertical-align:middle;margin-left:4px}
.radio.on{background:radial-gradient(#2f5d46 45%,#fff 50%)}
.bars td .b{height:10px;background:#2f5d46;border-radius:2px;display:inline-block;vertical-align:middle}
"""

import re as _re
def _ltr(h):
    h = _re.sub(r'(\d\d:\d\d–\d\d:\d\d)', r'<span dir="ltr">\1</span>', h)
    h = _re.sub(r'([−+][\d,]+ \([\d.]+%\))', r'<span dir="ltr">\1</span>', h)
    h = h.replace('(10,000 − 200)', '(<span dir="ltr">10,000 − 200</span>)')
    return h

def page(menu, active, user, content, extra=''):
    content, extra = _ltr(content), _ltr(extra)
    side = ''.join(f'<div class="{"on" if m == active else ""}">{E(m)}</div>' for m in menu)
    return f"""<!DOCTYPE html><html lang="he" dir="rtl"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="win"><div class="title"><b>בקרת דיווחי ייצור · בתי צמיחה מי עמי</b><span>{E(user)}</span><span class="wbtn"><span></span><span></span><span></span></span></div>
<div class="body"><div class="side">{side}</div><div class="main">{content}{extra}</div></div>
<div class="status"><span>נתוני דמה להמחשה בלבד</span><span>מחובר: {E(user)}</span></div></div></body></html>"""

def tbl(head, rows, cls=None):
    cls = cls or {}
    h = ''.join(f'<th>{x}</th>' for x in head)
    b = ''.join(f'<tr class="{cls.get(i, "")}">' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for i, r in enumerate(rows))
    return f'<table><tr>{h}</tr>{b}</table>'

def cards(items):
    return '<div class="cards">' + ''.join(f'<div class="card {c}"><div class="n">{n}</div><div class="l">{l}</div></div>' for n, l, c in items) + '</div>'

def field(label, val, cls=''):
    return f'<div class="f">{label}<span class="in {cls}">{val}</span></div>'

O, F, N = '<span class="tag open">פתוחה</span>', '<span class="tag fixed">תוקנה</span>', '<span class="tag negl">זניחה</span>'
PK = ['90412', '90415', '90433', '90437', '90451', '90458']

EXC_ROWS = [
    ['<span class="chk on"></span>', '22.11 07:42', PK[0], 'עגבנייה', 'העברה', 'פער כמות', '3%', 'דווחו 9,410 מתוך 9,800 צפויים', O],
    ['<span class="chk on"></span>', '22.11 07:42', PK[1], 'פלפל', 'שתילה', 'משך מרבי', '90 דק\'', 'משך 214 דק\'', O],
    ['<span class="chk"></span>', '22.11 07:42', PK[2], 'מלפפון', 'ריווח', 'דילוג שלב', '—', 'דווח ריווח בלי שתילה', O],
    ['<span class="chk"></span>', '21.11 07:35', PK[3], 'חציל', 'נעיצה', 'משך מרבי', '60 דק\'', 'שעת סיום חסרה', O],
    ['<span class="chk"></span>', '21.11 07:35', PK[4], 'עגבנייה', 'שתילה', 'פער כמות', '2%', 'דווחו 4,720 מתוך 4,900 צפויים', O],
]
EXC_HEAD = ['', 'מועד זיהוי', 'פק"ע', 'סוג צמח', 'שלב', 'סוג בדיקה', 'סף', 'תיאור הפער', 'סטטוס']

def exc_screen(extra_bar='', banner='', rows=None, extra=''):
    rows = rows or EXC_ROWS
    c = ('<h1>חריגות</h1><div class="sub">חריגות פתוחות, מהחדשה לישנה</div>' + banner +
         cards([('2', 'פער כמות', 'bad'), ('1', 'דילוג שלב', 'bad'), ('2', 'משך מרבי', 'bad'), ('5', 'סה"כ פתוחות', '')]) +
         '<div class="bar">' + field('מתאריך', '20.11.2026') + field('עד תאריך', '22.11.2026') + field('סטטוס', 'פתוחה ▾') +
         field('סוג בדיקה', 'הכול ▾') + field('שלב', 'הכול ▾') + field('סוג צמח', 'הכול ▾') + field('פק"ע', '&nbsp;') +
         '<span class="btn sec">סף זמני…</span>' + extra_bar + '</div>' +
         tbl(EXC_HEAD, rows, {0: 'sel', 1: 'sel'}) +
         '<div class="cols" style="margin-top:12px"><div class="panel" style="margin:0"><h3>חריגה נבחרת · פק"ע 90412 · העברה</h3>'
         'דיווח 7781203 · מכשיר MD-07 (אבי ל.) · 21.11.2026 · 06:10–08:05<br>תקינים 9,350 · פסולים 60 · סה"כ 9,410 מול 9,800 צפויים בשלב · פער 4.0% מול סף 3% (עגבנייה · העברה)'
         '<div class="note">הדיווח לא תוקן (גרסה 1)</div></div>'
         '<div style="flex:0 0 190px;display:flex;flex-direction:column;gap:8px;justify-content:flex-end"><span class="btn">סימון כזניחה (2)</span><span class="btn sec">פתיחת תיק פק"ע</span></div></div>')
    return page(TPI_MENU, 'חריגות', TPI_USER, c, extra)

S = {}

S['UC-1'] = ('ייבוא קובץ דיווחי ייצור', page(TPI_MENU, 'ייבוא קובץ', TPI_USER,
  '<h1>ייבוא קובץ פירוט דיווח ייצור</h1><div class="sub">קובץ Excel או CSV שיוצא מ-Priority</div>'
  '<div class="bar">' + field('קובץ', 'C:\\Exports\\production-report-2026-11-21.xlsx') + '<span class="btn sec">עיון…</span><span class="btn">ייבוא</span></div>'
  '<div class="panel"><h3>סיכום הייבוא · הושלם · 22.11.2026 07:38 · 18 שניות</h3>'
  '<div class="note" style="margin:0 0 10px">טווח הדיווחים בקובץ: 21.11.2026–21.11.2026</div>' +
  cards([('1,184', 'שורות חדשות', ''), ('37', 'שורות שתוקנו (גרסה חדשה)', 'amb'), ('12', 'שורות זהות', ''), ('3', 'שורות שנדחו', 'bad')]) +
  '<h3>פירוט השורות שנדחו</h3>' +
  tbl(['שורה בקובץ', 'מזהה דיווח', 'סיבת הדחייה'], [
      ['418', '7781522', 'חסר מזהה מכשיר'], ['902', '—', 'חסר מזהה דיווח'], ['1,077', '7781960', 'חסרה כמות תקינים']]) +
  '<div style="margin-top:12px;display:flex;gap:8px"><span class="btn">להרצת בדיקה</span><span class="btn sec">ייבוא קובץ נוסף</span></div></div>'))

S['UC-2'] = ('הרצת בדיקה', page(TPI_MENU, 'הרצת בדיקה', TPI_USER,
  '<h1>הרצת בדיקה</h1><div class="sub">השוואת הדיווחים שיובאו לספי החריגה</div>'
  '<div class="panel" style="margin-top:0"><h3>טווח הבדיקה</h3>'
  '<div style="margin-bottom:8px"><span class="radio on"></span> מאז ההרצה הקודמת (21.11.2026 07:31) · 1,221 דיווחים</div>'
  '<div style="display:flex;gap:10px;align-items:center"><span class="radio"></span> טווח תאריכים ' + field('מתאריך', '__.__.____') + field('עד תאריך', '__.__.____') + '</div>'
  '<div style="margin-top:12px"><span class="btn">הרצת בדיקה</span></div></div>'
  '<div class="panel"><h3>סיכום ההרצה · 22.11.2026 07:42 · 9 שניות</h3>' +
  cards([('1,221', 'דיווחים שנבדקו', ''), ('5', 'חריגות חדשות', 'bad'), ('4', 'חריגות שתוקנו', ''), ('2', 'פק"עות שנסגרו (מוכנות למכירה)', '')]) +
  tbl(['סוג בדיקה', 'חריגות חדשות', 'חריגות שתוקנו', 'סף שהופעל'], [
      ['פער כמות', '2', '3', 'כללי 2% · עגבנייה/העברה 3%'], ['דילוג שלב', '1', '0', 'כללי'], ['משך מרבי', '2', '1', 'לפי שלב']]) +
  '<div style="margin-top:12px"><span class="btn">לרשימת החריגות</span></div></div>'))

S['UC-3'] = ('צפייה בחריגות וסינון', exc_screen())

S['UC-4'] = ('סימון חריגה כזניחה', exc_screen(extra=
  '<div class="overlay"><div class="modal"><h3>סימון 2 חריגות כזניחות</h3>'
  'פק"ע 90412 · העברה · פער כמות<br>פק"ע 90415 · שתילה · משך מרבי'
  '<div class="f" style="margin-top:12px">סיבת הזניחות (חובה)<div class="ta">פער קטן מסף הספירה הידנית בשטח; אושר מול אחראית השטח</div></div>'
  '<div class="note">הסימון סוגר את החריגות. יירשמו מועד הסגירה והמשתמש שסימן.</div>'
  '<div style="margin-top:14px;display:flex;gap:8px;justify-content:flex-start"><span class="btn">אישור הסימון</span><span class="btn sec">ביטול</span></div></div></div>'))

S['UC-5'] = ('צפייה בכמות הצפויה של פק"ע', page(TPI_MENU, 'כמות צפויה', TPI_USER,
  '<h1>כמות צפויה של פק"ע</h1><div class="sub">כל שלב מושווה לכמות שנכנסה אליו: המתוכננת פחות הפסולים בשלבים הקודמים</div>'
  '<div class="bar">' + field('מספר פק"ע', '90412') + '<span class="btn">חיפוש</span></div>'
  '<div class="sub"><b>פק"ע 90412</b> · עגבנייה · <span class="tag open">פתוחה</span></div>' +
  cards([('10,000', 'כמות מתוכננת', ''), ('260', 'סך פסולים שדווחו', 'amb'), ('9,740', 'צפויה להמשיך לשלב הבא', '')]) +
  tbl(['שלב', 'צפוי בשלב', 'תקינים', 'פסולים', 'סה"כ דווח', 'פער', 'מול הסף'], [
      ['נעיצה', '10,000', '9,800', '200', '10,000', '0', '<span class="tag fixed">תקין</span>'],
      ['העברה', '9,800 <span class="muted">(אחרי 200 פסולים בנעיצה)</span>', '9,350', '60', '9,410', '−390 (4.0%)', '<span class="tag warnt">חוצה סף 3%</span>']], {1: 'hl'}) +
  '<div class="note">שלבים שטרם דווחו: שתילה, ריווח, מוכנות למכירה. הבא בתור, שתילה, צפוי לקבל 9,740.</div>'))

S['UC-6'] = ('צפייה בתיק פק"ע', page(TPI_MENU, 'תיק פק"ע', TPI_USER,
  '<h1>תיק פק"ע</h1><div class="bar">' + field('מספר פק"ע', '90412') + '<span class="btn">חיפוש</span></div>' +
  cards([('עגבנייה', 'סוג צמח', ''), ('זן לדוגמה', 'זן', ''), ('10,000', 'כמות מתוכננת', ''), ('העברה', 'שלב נוכחי', ''), ('פתוחה', 'סטטוס', '')]) +
  '<h3 style="margin:6px 0">דיווחים, לפי סדר השלבים</h3>' +
  tbl(['שלב', 'תאריך', 'מכשיר / עובד', 'שעות', 'תקינים', 'פסולים', 'גרסאות'], [
      ['נעיצה', '03.11.2026', 'MD-03 · רון מ.', '06:00–06:50', '9,800', '200', '<span class="tag ver">תוקן · 2 גרסאות</span>'],
      ['העברה', '21.11.2026', 'MD-07 · אבי ל.', '06:10–08:05', '9,350', '60', '1']], {0: 'hl'}) +
  '<h3 style="margin:12px 0 6px">חריגות של הפק"ע</h3>' +
  tbl(['מועד זיהוי', 'שלב', 'סוג בדיקה', 'תיאור הפער', 'סטטוס'], [
      ['22.11 07:42', 'העברה', 'פער כמות', 'דווחו 9,410 מתוך 9,800 צפויים', O],
      ['04.11 07:30', 'נעיצה', 'פער כמות', 'דווחו 9,600 מתוך 10,000 צפויים', F]])))

S['UC-7'] = ('צפייה בדיווחים מתוקנים', page(TPI_MENU, 'דיווחים מתוקנים', TPI_USER,
  '<h1>דיווחים מתוקנים</h1><div class="bar">' + field('מתאריך', '15.11.2026') + field('עד תאריך', '22.11.2026') +
  field('עובד', 'הכול ▾') + field('שלב', 'הכול ▾') + '<span class="btn">הצגה</span></div>' +
  tbl(['מזהה דיווח', 'פק"ע', 'שלב', 'מכשיר / עובד', 'תאריך', 'גרסאות', 'חריגה פתוחה'], [
      ['7780215', '90412', 'נעיצה', 'MD-03 · רון מ.', '03.11.2026', '2', '—'],
      ['7780954', '90437', 'נעיצה', 'MD-03 · רון מ.', '20.11.2026', '3', '<span class="tag open">פתוחה</span>'],
      ['7780611', '90451', 'העברה', 'MD-07 · אבי ל.', '18.11.2026', '2', '—']], {0: 'sel'}) +
  '<div class="panel"><h3>השוואת גרסאות · דיווח 7780215</h3>' +
  tbl(['שדה', 'גרסה 1 · ייבוא 04.11 07:26', 'גרסה 2 · ייבוא 22.11 07:38'], [
      ['שלב', 'נעיצה', 'נעיצה'], ['מכשיר', 'MD-03', 'MD-03'], ['שעות', '06:00–06:50', '06:00–06:50'],
      ['כמות תקינים', '9,400', '<span class="chg">9,800</span>'], ['כמות פסולים', '200', '200']]) +
  '<div class="note">השדות המסומנים שונו בגרסה החדשה. התיקון בוצע ב-Priority ונקלט בייבוא.</div></div>'))

S['UC-8'] = ('צפייה בתיק עובד', page(MGR_MENU, 'תיק עובד', MGR_USER,
  '<h1>תיק עובד</h1><div class="bar">' + field('שם עובד או מזהה מכשיר', 'אבי') + field('מתאריך', '01.10.2026') + field('עד תאריך', '22.11.2026') + '<span class="btn">חיפוש</span></div>' +
  tbl(['שם עובד', 'מזהה מכשיר'], [['אבי ל.', 'MD-07'], ['אבי ש.', 'MD-15']], {0: 'sel'}) +
  '<div class="sub" style="margin-top:12px"><b>אבי ל. · MD-07</b> · 01.10.2026–22.11.2026</div>' +
  cards([('146', 'דיווחים', ''), ('9', 'חריגות', 'bad'), ('6.2%', 'אחוז חריגות', 'amb'), ('5', 'דיווחים שתוקנו', '')]) +
  '<h3 style="margin:6px 0">חריגות לפי סוג בדיקה</h3>' +
  '<table class="bars"><tr><th>סוג בדיקה</th><th>חריגות</th><th></th></tr>'
  '<tr><td>פער כמות</td><td>5</td><td><span class="b" style="width:250px"></span></td></tr>'
  '<tr><td>משך מרבי</td><td>3</td><td><span class="b" style="width:150px"></span></td></tr>'
  '<tr><td>דילוג שלב</td><td>1</td><td><span class="b" style="width:50px"></span></td></tr></table>'))

S['UC-9'] = ('צפייה בחריגות פתוחות לפי ותק', page(TPI_MENU, 'חריגות לפי ותק', TPI_USER,
  '<h1>חריגות פתוחות לפי ותק</h1><div class="sub">מהחריגה הוותיקה ביותר</div>' +
  cards([('7', 'חריגות פתוחות', 'bad'), ('3.1 ימים', 'זמן טיפול ממוצע · 30 הימים האחרונים', '')]) +
  '<div class="bar">' + field('פתוחות יותר מ- (ימים)', '3') + '<span class="btn">סינון</span></div>' +
  tbl(['ימים פתוחה', 'מועד זיהוי', 'פק"ע', 'שלב', 'סוג בדיקה', 'תיאור הפער'], [
      ['<span class="red">6</span>', '16.11 07:30', '90398', 'ריווח', 'דילוג שלב', 'דווח ריווח בלי שתילה'],
      ['<span class="red">4</span>', '18.11 07:28', '90404', 'העברה', 'משך מרבי', 'משך 131 דק\'']], {0: 'hl', 1: 'hl'}) +
  '<div class="note">מוצגות 2 מתוך 7 החריגות הפתוחות: אלה שפתוחות יותר מ-3 ימים</div>'))

S['UC-10'] = ('שיוך שם עובד למכשיר', page(TPI_MENU, 'מכשירים ועובדים', TPI_USER,
  '<h1>מכשירים ועובדים</h1><div class="sub">שם העובד לא מגיע מ-Priority. מכשיר בלי שם מוצג לפי המזהה שלו.</div>' +
  tbl(['מזהה מכשיר', 'שם עובד', 'דיווח אחרון', ''], [
      ['MD-03', 'רון מ.', '21.11.2026', '<span class="btn sec">עריכה</span>'],
      ['MD-07', 'אבי ל.', '21.11.2026', '<span class="btn sec">עריכה</span>'],
      ['MD-15', 'אבי ש.', '20.11.2026', '<span class="btn sec">עריכה</span>'],
      ['MD-19', '<span class="in err" style="min-width:160px">&nbsp;</span> <span class="red">חובה להזין שם</span>', '21.11.2026', '<span class="btn">שמירה</span>'],
      ['MD-22', '<span class="tag warnt">לא שויך שם</span>', '19.11.2026', '<span class="btn sec">שיוך</span>']], {3: 'sel', 4: 'hl'})))

S['UC-11'] = ('הפקת דוח מגמות לפי גידול', page(MGR_MENU, 'דוח לפי גידול', MGR_USER,
  '<h1>דוח מגמות לפי סוג גידול</h1><div class="bar">' + field('תקופה', 'חודש ▾') + field('מתאריך', '23.10.2026') + field('עד תאריך', '22.11.2026') +
  '<span class="btn">הפקה</span><span class="btn sec">ייצוא ל-Excel</span></div>' +
  tbl(['סוג צמח', 'דיווחים', 'חריגות', 'אחוז חריגות', 'תקופה קודמת', 'שינוי', 'פער כמות', 'דילוג שלב', 'משך מרבי'], [
      ['עגבנייה', '4,812', '96', '2.0%', '2.6%', '<span style="color:#1f6b3a">▼ 0.6</span>', '61', '9', '26'],
      ['פלפל', '3,207', '83', '2.6%', '2.1%', '<span class="red">▲ 0.5</span>', '40', '6', '37'],
      ['מלפפון', '2,145', '30', '1.4%', '1.5%', '<span style="color:#1f6b3a">▼ 0.1</span>', '18', '4', '8'],
      ['חציל', '1,388', '41', '3.0%', '3.1%', '<span style="color:#1f6b3a">▼ 0.1</span>', '22', '5', '14']]) +
  '<div class="note">התקופה הקודמת: 23.09.2026–22.10.2026 (אותו אורך)</div>'))

S['UC-12'] = ('הפקת דוח מגמות לפי פעולה ושלב', page(MGR_MENU, 'דוח לפי פעולה ושלב', MGR_USER,
  '<h1>דוח מגמות לפי פעולה ושלב</h1><div class="bar">' + field('תקופה', 'חודש ▾') + field('מתאריך', '23.10.2026') + field('עד תאריך', '22.11.2026') + '<span class="btn">הפקה</span></div>' +
  cards([('3.1 ימים', 'זמן טיפול ממוצע בחריגות שנסגרו', ''), ('4.2 ימים', 'בתקופה הקודמת', '')]) +
  tbl(['שלב / פעולה', 'חריגות', 'אחוז חריגות', 'אחוז דיווחים שתוקנו', 'משך ממוצע', 'אחוז חריגות · תקופה קודמת'], [
      ['נעיצה', '58', '2.4%', '1.9%', '72 דק\'', '2.9%'], ['העברה', '71', '3.1%', '2.8%', '48 דק\'', '2.7%'],
      ['שתילה', '64', '2.2%', '2.0%', '96 דק\'', '2.3%'], ['ריווח', '39', '1.6%', '1.1%', '41 דק\'', '1.8%'],
      ['מוכנות למכירה', '18', '0.9%', '0.7%', '35 דק\'', '1.0%']], {1: 'hl'})))

S['UC-13'] = ('ניהול ספי חריגה', page(TPI_MENU, 'ספי חריגה', TPI_USER,
  '<h1>ספי חריגה</h1><div class="sub">הסף המפורט ביותר גובר על הכללי. שינוי חל מהבדיקה הבאה.</div>'
  '<div style="margin-bottom:10px"><span class="btn">+ סף חדש</span></div><div class="cols"><div style="flex:1.6">' +
  tbl(['סוג בדיקה', 'סוג צמח', 'שלב', 'ערך', 'סטטוס', 'חריגות ב-30 יום'], [
      ['פער כמות', 'כל הסוגים', 'כל השלבים', '2%', 'פעיל', '142'],
      ['פער כמות', 'עגבנייה', 'העברה', '3%', 'פעיל', '11'],
      ['משך מרבי', 'כל הסוגים', 'שתילה', '90 דק\'', 'פעיל', '38'],
      ['משך מרבי', 'כל הסוגים', 'נעיצה', '60 דק\'', 'פעיל', '21'],
      ['דילוג שלב', 'כל הסוגים', 'כל השלבים', '—', 'פעיל', '24'],
      ['פער כמות', 'פלפל', 'כל השלבים', '4%', '<span class="muted">לא-פעיל</span>', '0']], {1: 'sel'}) +
  '</div><div class="panel" style="margin:0"><h3>עדכון סף</h3>' +
  field('סוג בדיקה', 'פער כמות') + '<br>' + field('סוג צמח', 'עגבנייה') + '<br>' + field('שלב', 'העברה') + '<br>' +
  field('ערך (%)', '3') + '<br>' + field('הערה', 'הוסכם מול צוות האגרונומים') + '<br>' + field('סטטוס', 'פעיל ▾') +
  '<div style="margin-top:12px;display:flex;gap:8px"><span class="btn">שמירה</span><span class="btn sec">ביטול</span><span class="btn sec">מחיקה</span></div>'
  '<div class="note">עודכן ע"י נטלי · 10.11.2026</div></div></div>'))

S['UC-14'] = ('ניהול משתמשים', page(MGR_MENU, 'משתמשים', MGR_USER,
  '<h1>משתמשים</h1><div class="bar">' + field('תפקיד', 'הכול ▾') + field('סטטוס', 'הכול ▾') + '<span class="btn">+ משתמש חדש</span></div><div class="cols"><div style="flex:1.6">' +
  tbl(['שם מלא', 'שם משתמש', 'תפקיד', 'מנהל מערכת', 'סטטוס'], [
      ['אוריאל', 'user01', 'מנכ"ל', 'לא', 'פעיל'], ['דותן', 'user02', 'מנהל תפעול וייצור', 'כן', 'פעיל'],
      ['נטלי', 'user03', 'אחראית תפ"י', 'לא', 'פעיל'], ['משתמש בדיקה', 'user04', 'אחראית תפ"י', 'לא', '<span class="muted">לא-פעיל</span>']], {2: 'sel'}) +
  '</div><div class="panel" style="margin:0"><h3>עדכון משתמש</h3>' +
  field('שם מלא', 'נטלי') + '<br>' + field('שם משתמש', 'user03') + '<br>' + field('דוא"ל', 'user03@example.com') + '<br>' +
  field('תפקיד', 'אחראית תפ"י ▾') + '<br><div><span class="chk"></span> מנהל מערכת</div><br>' + field('סטטוס', 'פעיל ▾') +
  '<div style="margin-top:12px;display:flex;gap:8px"><span class="btn">שמירה</span><span class="btn sec">ביטול</span><span class="btn sec">מחיקה</span></div>'
  '<div class="note">שינוי הרשאות חל מהכניסה הבאה של המשתמש</div></div></div>'))

S['UC-16'] = ('שינוי סף זמני', exc_screen(
  extra_bar='<span style="border-right:2px solid #e0b46a;padding-right:10px;display:flex;gap:8px;align-items:flex-end">' +
            field('סף זמני · פער כמות', '3.8%') + '<span class="muted" style="font-size:12px">שמור: 2% כללי · 3% עגבנייה/העברה</span><span class="btn warn">ביטול סף זמני</span></span>',
  banner='<div class="banner">תצוגה לפי סף זמני: פער כמות 3.8% במקום הספים השמורים. עם הסף הזמני היו נשארות 1 מתוך 2 חריגות פער כמות. הסף השמור והחריגות לא שונו.</div>',
  rows=[['<span class="chk on"></span>', '22.11 07:42', PK[0], 'עגבנייה', 'העברה', 'פער כמות', '<s>3%</s> 3.8%', 'דווחו 9,410 מתוך 9,800 צפויים <span class="muted">(4.0%)</span>', O],
        EXC_ROWS[1], EXC_ROWS[2], EXC_ROWS[3],
        ['<span class="chk"></span>', '<span class="muted">21.11 07:35</span>', '<span class="muted">90451</span>', '<span class="muted">עגבנייה</span>', '<span class="muted">שתילה</span>', '<span class="muted">פער כמות</span>', '<s>2%</s> 3.8%', '<span class="muted">דווחו 4,720 מתוך 4,900 צפויים (3.7%) · לא נשארת בסף הזמני</span>', O]]))

ORDER = ['UC-1', 'UC-2', 'UC-3', 'UC-4', 'UC-5', 'UC-6', 'UC-7', 'UC-8', 'UC-9', 'UC-10', 'UC-11', 'UC-12', 'UC-13', 'UC-14', 'UC-16']

if __name__ == '__main__':
    import os
    from playwright.sync_api import sync_playwright
    os.makedirs('/home/claude/work/screens/html', exist_ok=True)
    os.makedirs('/home/claude/work/screens/png', exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        pg = b.new_page(viewport={'width': 1282, 'height': 802}, device_scale_factor=1.5)
        for k in ORDER:
            name, html = S[k]
            fn = 'screen-' + k.lower()
            open(f'/home/claude/work/screens/html/{fn}.html', 'w', encoding='utf8').write(html)
            pg.set_content(html)
            pg.locator('.win').screenshot(path=f'/home/claude/work/screens/png/{fn}.png')
            print('ok', fn)
        b.close()
