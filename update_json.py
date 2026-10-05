import json

new_q8 = 'người 40x80 lệch khoảng 6 pixel là oks dưới 0.5 còn người 250x500 thì khoảng 41 pixel. sigma của mắt nhỏ vì mắt là điểm cố định dễ xác định. với camera trên cao người bé nên đoán lệch mắt một chút thôi là bị trừ điểm rất nặng'

new_q11 = 'lỗi thứ nhất ở bức ảnh con hổ đi ngang qua là nhầm chân trái phải làm các nét vẽ bị chéo nhau do chân hổ trông khá giống nhau. cách sửa là lật ảnh đúng chuẩn khi huấn luyện để máy học kỹ hơn. lỗi thứ hai trong ảnh con hổ nằm ở bãi cỏ là các khớp đuôi bay lơ lửng do bị che khuất. cách khắc phục là báo cho máy biết điểm nào bị che để máy không cố đoán mò'

try:
    with open("submission/ket_qua.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    if "answers" in data:
        data["answers"]["Q8"] = new_q8
        data["answers"]["Q11"] = new_q11

    with open("submission/ket_qua.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
except Exception as e:
    print(e)
