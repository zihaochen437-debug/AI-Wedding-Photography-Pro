# 视频正式生产体系

视频是核心产品，不是 Future。照片与视频共享 AB01–AB06，不建立“视频版新娘/新郎”。

## 1. 两条路线

### PERSON_DRIVEN_VIDEO
基于人物、Look、Scene 从零策划婚纱动态镜头、短片、爱情短片、微电影、剧情/情绪片、电影预告、婚礼邀请、时尚广告、旅行/纪录感、新中式、民国或自定义。

### PHOTO_TO_VIDEO
基于已批准婚纱照片制作动态肖像、单图/多图动态、情绪/剧情短片、婚纱 MV、动态相册、电影式片段、社交短视频。

## 2. VIDEO_PROJECT_GATE

确认视频类型、数量、目标时长、横/竖、比例、用途/发布平台、风格、情绪、动态强度、音乐/环境声/旁白/对白。人物剧情还要确认真实故事 / AI 虚构 / 真实信息+创作改编；AI 编写内容不得冒充用户真实经历。

## 3. VB01

`VB01｜婚纱视频分镜与时间轴资产板`：Video ID、名称、版本、类型、时长、比例、用途、故事、人物、Suite、Look、Scene、音乐、环境音、旁白/对白、Storyboard、Timeline、Shot/Segment、时间区间、动作、表情、Camera Movement、Scene Area、Sound Event、Transition、Reference Binding、Status。

## 4. 时间轴与导演描述

视频 Prompt 不能只写“让照片动起来”。按 0–3s / 3–7s / 7–11s 等合理连续时间段写人物位置、动作速度、情绪变化、Camera 路径、环境运动、光线变化、声音事件和最终收束。时间不能重叠、无意义空段或突然跳动作。

## 5. 物理

控制人体关节、重心、步态、惯性、脚地接触、裙摆重量、头纱、发丝、风、水、植物与 Camera Movement。禁止滑行、漂浮、身体融化、手穿身体、衣服穿模、逐帧换脸、身高变化、服装突然改款、Scene 固定物体随机消失。

## 6. 参考职责

概念参考可为：@图片1 新娘 Look、@图片2 新郎 Look、@图片3 双人比例（需要时）、@图片4 Scene、@图片5 Storyboard/Keyframe、@视频1 动作/运镜、@音频1 节奏/旁白。每份参考明确控制范围和非继承范围。

## 7. Photo-to-Video

Approved Wedding Photo 是视觉锚点，目标是“这张照片沿时间继续发生”。默认只添加呼吸、眨眼、轻微微笑/转头、自然手部微动作、头纱/裙摆/头发、草木/水/云、受控 Dolly/Pan/Orbit；不得默认改变脸、婚纱、礼服、珠宝、建筑、关键道具、站位几何和身高比例。

## 8. 视频 QC 与修订

检查身份、同脸/交换、身高体型、妆发、婚纱/礼服、手、道具、Scene、Camera、Flicker/Morphing、群演复制、音画同步、口型（适用）、剧情节奏。

片段错误使用 Segment Scoped Revision，只开放目标时间段和目标域。Approved Video 是最终视频基线；后续只做片段编辑、延长、拼接、超分、声音、多轨、编码/输出，不默认重生一条“最终视频”。

## 9. Audio Boundary

音频控制时间、节奏、情绪和语音，不控制视觉身份。声音克隆/模仿仅在当前平台真实支持且用户明确授权时使用。

## 10. Runtime Contract

只有 `VIDEO_GENERATION_CALLABLE = VERIFIED` 才能声称实际生成；UNKNOWN/UNSUPPORTED 时只输出完整 VB01、时间轴、Prompt、参考绑定和用户可执行步骤，不假装已经生成。
