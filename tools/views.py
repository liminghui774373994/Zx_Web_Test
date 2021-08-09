from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def test(request):
    result = {
    "error_code": 0,
    "message": "ok",
    "data": {
        "list": [
            {
                "id": 1,
                "name": "对比题目总数及各题型题目数",
                "result": 'fail',
                "datail": "[9783, 6080, 3113, 590],迁移前老题库库题目总数: 8656 --主观题: 5532 --选择题: 2743 --是非题: 381 迁移后临时库题目总数: 9783 --主观题: 6080 --选择题: 3113 --是非题: 590"
            },
            {
                "id": 2,
                "name": "数据逐条比对questions表和brush_questions表",
                 "result": 'fail',
                "datail":  "迁移失败：迁移前后数据不一致"
            },
            {
                "id": 3,
                "name": "确认brush_questions迁移后solve_cnt字段",
                 "result": 'pass',
                "datail":  ""
            },
            {
                "id": 4,
                "name": "数据逐条比对brush_question_answers表",
                 "result": 'fail',
                 "datail":  "本次有 12703 个主观题的答案需要迁移, 实际有 13700 个主观题的答案完成迁移"
            },
            {
                "id": 5,
                "name": "数据逐条比对brush_question_options表",
                "result": 'fail',
                "datail":  "本次有 8655 个选择题的答案需要迁移实际有 9737 个选择题的答案完成迁移 本次有 762 个是非题的答案需要迁移  实际有 1182 个是非题的答案完成迁移"
            }]
    }
    }
    return JsonResponse(result,content_type='application/json', charset='utf-8')

