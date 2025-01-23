import os
import shutil

# File mapping
file_mapping = {
    '3. 📅 Day1 教程：认识结构化提示词 - 告别"抽卡式生成".md': 'lessons/day1-basics.md',
    '4.📅 Day2 教程：环境设定三板斧 —— 像搭积木一样布置你的"小世界".md': 'lessons/day2-environment.md',
    '5. 📅 Day3 教程：角色控制 —— 从"木头人"到"活人"的秘诀.md': 'lessons/day3-character.md',
    '6.📅 Day4 教程：镜头语言速成 —— 用手机拍摄思维控制AI运镜.md': 'lessons/day4-camera.md',
    '7.📅Day5：动态元素控制.md': 'lessons/day5-dynamics.md',
    '8.📅Day6：时间轴管理 —— 像剪辑软件一样打关键帧.md': 'lessons/day6-timeline.md',
    '9.📅Day7：多元素交互 —— 角色与环境的化学反应.md': 'lessons/day7-interaction.md',
    '10.📅Day8：风格融合术 —— 打破次元壁的美学公式.md': 'lessons/day8-style.md',
    '11.📅Day9：异常处理 —— 当AI叛逆时的急救手册.md': 'lessons/day9-troubleshooting.md',
    '12.📅 Day10 教程：完整项目实战 —— 15秒短视频从0到1全流程.md': 'lessons/day10-project.md'
}

# Move files
for src, dst in file_mapping.items():
    try:
        if os.path.exists(src):
            shutil.move(src, dst)
            print(f'Moved {src} to {dst}')
        else:
            print(f'Source file not found: {src}')
    except Exception as e:
        print(f'Error moving {src}: {e}') 