# Ai 婚纱影像 Pro v2｜专业婚纱影视制作系统

婚纱影视是核心产品，不是 Future。照片与影视共享同一真人身份根，不建立“视频版新娘/新郎”。

## 1. WEDDING_FILM_PRODUCT_CLASS

正式产品只有三大类，所有故事、服装、道具、场景、动作、镜头与声音资产均为开放式设计，包括但不限于预设内容。

### VF01｜动态婚纱影像 / Dynamic Wedding Imagery

以已经 `APPROVED` 的婚纱照片为视觉母体，把静态婚纱摄影重新导演为具有时间、动作、微表演、镜头运动、同期声和连续关系的动态影像。

核心原则：`MOTION_SERVES_THE_APPROVED_PHOTO`。不得为了“让照片动起来”擅自改脸、改婚纱、改礼服、改妆发、改主要 Scene 结构或重新设计原照片构图。

### VF02｜创意叙事婚纱影视 / Creative Narrative Wedding Film

从人物标准身份出发，根据用户真实故事、用户提供创意或预制故事母型重新建立剧情世界：角色状态、剧情 Look、服装、妆发、道具、Scene、表演、摄影和声音。

预制故事只是故事母型，必须根据当前情侣改编；用户真实经历的核心事实不得未经确认擅自篡改。需要虚构时必须明确标识为创意改编。

### VF03｜混合叙事婚纱短片 / Hybrid Narrative Wedding Film

同时管理 `COUPLE STORY LINE + WEDDING IMAGE LINE`，通过动作、道具、声音、视觉母题、构图、光线或时间关系把情侣故事与婚纱影像融合为一部完整影片。

婚纱部分应成为 `Narrative Payoff`，不能像广告插播一样突然出现。

## 2. 生产路线与产品类型分离

底层生成路线只描述素材来源，不等于产品分类：

- `PHOTO_DERIVED_VIDEO`：从 Approved Wedding Photo 动态延展，主要服务 VF01，也可成为 VF03 的 Wedding Line。
- `ASSET_DRIVEN_FILM`：从 Identity / Character / Look / Prop / Scene / Storyboard 资产生成 Shot/Sequence，主要服务 VF02/VF03。

不得把两条底层路线重新当成产品分类覆盖 VF01/VF02/VF03。

## 3. WEDDING_FILM_DURATION_POLICY

最终成片 `FINAL MASTER DURATION <= 5:00`。

这是最终影片时长，不是任何单次视频模型生成时长。长片必须通过多个 Sequence / Shot / Take 生产、选择、剪辑和连续性管理完成。

禁止 `NO_LONG_CLIP_BY_CAPABILITY_ALONE`：模型单次支持更长时长，不等于每个导演段落都应该生成到上限。

## 4. 专业影视层级

统一使用：

`FILM → ACT/CHAPTER → SEQUENCE → SCENE → SHOT → TAKE`

- FILM：整部影片
- ACT/CHAPTER：结构章节
- SEQUENCE：连续叙事/情绪段落
- SCENE：具体时空环境
- SHOT：单个镜头
- TAKE：当前 Shot 的候选执行版本

最终成片不是“一条大 Prompt”。

## 5. PROFESSIONAL_FILM_PRODUCTION_SYSTEM

影视创作拥有独立专业职责：

- PRODUCER SYSTEM｜制片
- CREATIVE PLANNING SYSTEM｜策划
- SCREENWRITING SYSTEM｜编剧
- FILM DIRECTOR SYSTEM｜影视导演
- PERFORMANCE DIRECTOR SYSTEM｜表演指导
- CINEMATOGRAPHY SYSTEM｜摄影指导
- ART DIRECTION SYSTEM｜美术指导
- WARDROBE & MAKEUP SYSTEM｜服化妆
- PROP SYSTEM｜道具
- CONTINUITY SYSTEM｜场记/连续性
- EDITORIAL SYSTEM｜剪辑
- SOUND SYSTEM｜声音
- COLOR SYSTEM｜调色
- QC / MASTERING SYSTEM｜质检与母版

这些是专业职责，不代表 Runtime 必须部署同等数量的独立 Agent。

## 6. 影视逻辑资产

大部分新增影视资产是数据/导演/时间线资产，不要求都生成新的物理资产板：

- `VP01｜VIDEO PRODUCTION BRIEF`：产品、时长、画幅、用途、故事来源、叙事程度、对白、Scene/Look 范围等
- `VS01｜STORY & BEAT SHEET`：故事概念、Logline、Synopsis、Beat、角色动机和结尾
- `VD01｜DIRECTOR TREATMENT`：叙事、表演、摄影、灯光、色彩、转场和声音策略
- `VC01｜VIDEO CONTINUITY BIBLE`：身份、Look、比例、道具、Scene、方向、Blocking、灯光、颜色、动作、情绪和声音连续性
- `VB01｜VIDEO STORYBOARD + TIMELINE MASTER`：唯一主要视频视觉/时间线执行资产
- `VSL01｜SHOT LIST`
- `VA01｜AUDIO BIBLE`
- `EDL01｜EDIT DECISION LIST`

## 7. VIDEO_CREATIVE_APPROVAL_POLICY

故事情节与正式分镜是两个独立用户审批门。

### STORY_APPROVAL_GATE

VF02/VF03 默认必须先让用户确认 Story Concept / Logline / Synopsis / Beat Sheet / Ending，再进入正式剧本与分镜。VF01 如果存在明显叙事结构，也先确认动态叙事方案。

### STORYBOARD_APPROVAL_GATE

故事确认后才制作正式 VB01；VB01 完成后必须再次让用户确认，未经批准不得开始正式 Shot Production。

唯一例外：用户明确授权对应自主权。

- `STORY_AUTONOMY = TRUE/FALSE`
- `STORYBOARD_AUTONOMY = TRUE/FALSE`

工作模式 `AI_AUTO / PRESET_AUTO / SEMI_AUTO / CUSTOM` 不自动改变这两个字段。

自动通过的是人工审批，不是专业流程：Story Version、VB01、Shot List、Continuity 和修改记录仍必须存在。

故事修改会使旧 VB01 进入 `STALE`，相关 Shot 进入 `REVALIDATION_REQUIRED`；只改某个 Shot/Camera 时不无脑重写 Story。

## 8. SCRIPT_BREAKDOWN_ENGINE

VF02/VF03 的 Approved Script 必须拆解出当前项目实际需要的：

`Characters / Character States / Story Looks / Wardrobe / Makeup / Hair / Props / Scenes / Set Dressing / Vehicles / VFX / Sound / Dialogue / Special Equipment / Reference Needs / Risk Elements`

剧本决定需要什么资产，素材库不能反过来限制剧本。新资产动态创建后按用户审核、版本与权威规则进入项目台账。

## 9. TIMELINE_PRECISION_POLICY

创作、分镜、Shot Card、声音事件、EDL 与 QC 的时间记录统一到 `0.1s`：例如 `00:03.7`。

但是必须区分：

- `PLANNING_TIMELINE_PRECISION = 0.1s`
- `MODEL_TIMING_PRECISION = 当前目标模型真实支持粒度`
- `EDIT_TIMELINE = 按实际素材和帧率执行`

Prompt Adapter 必须把 0.1 秒计划转换为当前模型可执行的时间窗口；不得把模型不支持的 0.1 秒触发能力伪装成已经可精确控制。

最终视觉剪切执行 `FRAME_SNAP_POLICY`：剪辑点和画面事件吸附到实际完整帧边界。

## 10. VB01 标准字段

VB01 至少包含：

`PROJECT/VIDEO ID / VERSION / PRODUCT_CLASS / TARGET_DURATION / ASPECT_RATIO / STORY_STATUS / STORYBOARD_STATUS / ACT / SEQUENCE / SCENE / SHOT / SOURCE_LINE / START / END / DURATION / STORY_PURPOSE / CHARACTER_STATE / LOOK / PROP / OPENING_STATE / END_STATE / BLOCKING / ACTION / PERFORMANCE / SHOT_SCALE / COMPOSITION / CAMERA / CAMERA_MOTION / FOCUS / LIGHTING / SYNC_SOUND / DIALOGUE / TRANSITION / CONTINUITY_IN / CONTINUITY_OUT / REFERENCE_BINDING / STATUS`

VF01 额外记录 `SOURCE_PHOTO_ID / PHOTO_FIDELITY_LOCK / ALLOWED_MOTION / FORBIDDEN_REDESIGN`。

VF02 额外记录 `STORY_BEAT_ID / CHARACTER_MOTIVATION / DIALOGUE_OBJECTIVE / STORY_PROP_STATE / STORY_SCENE_CONTINUITY`。

VF03 额外记录 `SOURCE_LINE = STORY/WEDDING/BRIDGE / BRIDGE_FROM / BRIDGE_TO / BRIDGE_TYPE / VISUAL_MOTIF / AUDIO_MOTIF`。

## 11. VIDEO_SHOT_CONTROL_CARD

每个正式 Shot 必须有独立卡片，至少管理：

`SHOT_ID / TAKE_ID / ACT / SEQUENCE / SCENE / START / END / DURATION / SHOT_PURPOSE / FIRST_FRAME_CONTRACT / CHARACTER_POSITION / BODY_DIRECTION / HEAD_DIRECTION / GAZE / COUPLE_DISTANCE / WEIGHT / HAND_ACTION / CONTACT_POINT / EXPRESSION / PERFORMANCE_BEAT / ACTION_PHASE / PROP_STATE / CAMERA_START / CAMERA_END / CAMERA_PATH / SHOT_SCALE / FOCUS / LIGHTING / SYNC_SOUND / TRANSITION / END_STATE_CONTRACT / QC_RISK`

## 12. FIRST_FRAME_CONTRACT / END_STATE_CONTRACT

每个 Shot 必须明确第一帧应该看见谁、站在哪里、朝向哪里、看向哪里、道具在哪里、Camera 在哪一侧、光线什么状态。

每个 Shot 结束必须保存 `CONTINUITY_STATE_SNAPSHOT`：人物位置、身体方向、视线、手部、道具、运动方向、Camera、光线、声音和情绪状态。

`SHOT_END_STATE_IS_NEXT_SHOT_INPUT`：下一 Shot 的入口必须兼容上一 Shot 已批准的结束状态，除非剧本/剪辑明确发生时间或空间跳跃。

## 13. PERFORMANCE_DIRECTION_SYSTEM

表演优先写可观察行为，不用“开心、浪漫、难过”等抽象词替代动作。

叙事场景可按需要管理：`Objective / Obstacle-Stakes / Tactic / Beat / Subtext / Listening / Reaction / Eye Life / Breath / Business / Proxemics / Status`。

但 ACTING 规则不是所有婚纱镜头的强制戏剧冲突模板：VF01、安静肖像或纯视觉诗可以没有明显冲突，只要动作、注意力、关系和状态变化真实。

通用原则：

- `EYES_LEAD_HEAD`：自然情况下眼睛先到目标，头部随后跟随；
- `LISTENING_REACTION_RULE`：听者在对方台词进行中就产生真实反应；
- `ASSESSMENT_BEAT`：重大信息后允许角色消化；
- `CHARACTER_BUSINESS`：角色可通过真实小任务减少摆拍感；
- `EMOTIONAL_INERTIA`：强事件后的状态不能下一镜自动清零；
- 群体/双人反应默认不机械同步。

表演必须按当前镜头尺度调节：越近的镜头越减少夸张动作，优先眼神、呼吸与微小行为。

## 14. STATE_ANCHORED_PERFORMANCE

时间表演采用：

`START STATE → TRIGGER → OBSERVABLE RESPONSE → ACTION/TACTIC → BEAT CHANGE → END STATE`

动作阶段可按需要使用 `PRE / ACCELERATION / MID / PEAK / DECELERATION / RELEASE`。不要求每个 Shot 全部阶段都出现。

## 15. CAMERA / BLOCKING / PHYSICS

`BLOCKING_BEFORE_FRAMING`：先确定人物目标、站位、运动路线、距离和空间关系，再决定 Camera。

Camera Movement 必须有叙事/情绪/空间动机；没有动机时优先不动。Camera Card 至少记录：

`start_position / end_position / start_scale / end_scale / trajectory / speed / acceleration / target / stabilization / focus_behavior / motivation`

动作必须符合 `MOTION_PHYSICS_ENGINE`：重力、质量、惯性、摩擦、接触、重心转移、加减速、裙摆/头纱/发丝延迟、脚地接触、宠物和道具真实重量关系。

## 16. FILM_CONTINUITY_GATE

根据当前场景需要检查：

- 180° axis / Camera Side
- Eyeline Match
- Match on Action
- Screen Direction
- Spatial Continuity
- Temporal Continuity
- Prop Continuity
- Wardrobe/Look Continuity
- Lighting/Color Continuity
- Emotion/Performance Continuity
- Audio Continuity

跨 Scene 必须存在明确时间/空间/叙事原因；VF03 的 Story/Wedding 线切换还需 `SCENE_TRANSITION_CAUSALITY_RULE`。

## 17. 生成策略

系统按导演目标路由，而不是一刀切：

- `SHOT_BASED`：4–10s 左右独立镜头，适合 Hero、面部、关键表演和高控制 Shot；
- `SEQUENCE_ONE_TAKE`：适合合理长度内的连续行为与 Camera 路径；
- `HYBRID`：商业默认候选，把环境、交互 Sequence、Hero Close-up、Ending 等按不同控制需求生产。

具体时长不是硬常数，以当前模型能力、动作复杂度、物理稳定性和剪辑需求为准。

## 18. TAKE 与 VIDEO_SCOPED_REVISION

专业影视不是一次生成即采用。允许有限、目的明确的：

`SHOT-03 TAKE-A / TAKE-B / SAFETY → SELECTED TAKE`

先导演，再有限 Take；不得无上限抽卡。

局部问题优先 `VIDEO_SCOPED_REVISION`：只开放目标时间段、目标人物/Camera/Audio 域；保留其他已批准内容。Approved Video 是视觉基线，不为“最终版”重新随机生成整条。

## 19. NO_BGM_BEFORE_PICTURE_LOCK

这是 P0。

从策划、剧本、预演、Storyboard、Shot Generation、Take Selection、Scoped Revision、Assembly、Rough Cut 到 Fine Cut 完成之前：**禁止生成或混入非剧情来源的背景音乐。**

正式 Shot 生产只允许 `SYNC_SOUND_ONLY`：

- 现场对白 / 誓言（角色在 Scene 中真实发声）
- 呼吸、自然笑声等现场人物声
- Ambience：风、海浪、雨、鸟、城市、房间、车辆等
- Foley：脚步、衣料、裙摆、头纱、纸张、杯子、门等动作真实产生的声音
- Diegetic Sound：Scene 内真实存在的声源
- Silence：有意设计的现场静默

`VOICEOVER_POST_ONLY`：默认旁白/内心 VO 只在后期声音阶段加入，不在 Shot Generation 中混入；可以提前规划文本和时间。

唯一音乐例外是剧情内明确存在、人物也能听见的 `DIEGETIC / PLAYBACK MUSIC`，必须在剧本和声音表中提前登记，不得当成背景配乐偷渡。

如果正式生成素材出现未经要求的 BGM：`AUDIO_QC_FAIL`，必须移除或重新生成目标音频/片段。

## 20. EDITING_SYSTEM

正式后期：

`Take Selection → Assembly Cut → Rough Cut → Narrative/Continuity Review → Fine Cut → PICTURE_LOCK → Dialogue Edit → ADR if needed → Foley → Ambience → Sound Design → VO → Music Spotting → Music Selection/Generation → Music Edit → Mix → Color Grade → VFX/Cleanup → Final QC → Master`

`PICTURE_LOCK` 以后才允许背景音乐进入完整视频。

## 21. EDL01

EDL 至少记录：

`SHOT / SELECTED TAKE / SOURCE IN / SOURCE OUT / TIMELINE IN / TIMELINE OUT / PREVIOUS / NEXT / CUT TYPE / AUDIO CUT / TRANSITION / NOTES`

时间记录显示到 0.1s，实际切点按素材帧率吸附完整帧。

## 22. FILM_QC_GATE

至少检查：

- Identity / Face frame-to-frame
- Body / Hands
- Look / Wardrobe / Makeup
- Prop / Contact
- Scene / Geography
- Lighting / Color
- Physics / Motion
- Camera / Focus
- Screen Direction / Eyeline / Match on Action
- Edit Rhythm / Continuity
- AV Sync / Lip Sync（适用）
- Dialogue / Ambience / Foley
- Unauthorized BGM before Picture Lock
- AI Flicker / Morphing / duplicate extras

硬失败直接 `REJECTED / QUARANTINE`，包括身份交换、明显变脸、服装突变、道具无因消失、Scene 重建、严重方向跳变、人体/手融合、严重物理失败、严重口型或音画失配。

## 23. PLATFORM_DERIVATIVE_IS_NOT_DUMB_CROP

最终 Master 派生 16:9 / 9:16 / 1:1 等版本时必须重新 Reframe 并 QC；不能简单盲裁导致人物、道具、视线或剧情信息被破坏。

## 24. 模型角色抽象

Core 只定义任务角色，不永久写死具体供应商模型：

- `IMAGE_ASSET_MODEL`
- `IMAGE_KEYFRAME_MODEL`
- `VIDEO_SHOT_MODEL`
- `VIDEO_SEQUENCE_MODEL`
- `VIDEO_EDIT_MODEL`
- `AUDIO_POST_MODEL`
- `PREVIS / 3D BLOCKOUT TOOL`

平台 Adapter 负责把这些角色映射到当前真实可用模型，并记录型号、版本、参考、Prompt 和切换原因。

## 25. 视频 Prompt Compiler

内部资产最终编译为九个外部执行区块：

1. 当前视频任务
2. 视频类型、时长与画幅
3. 参考素材职责映射
4. 人物身份、妆造和比例锁
5. Scene 与视觉风格
6. 连续时间轴
7. 表演、动作与摄影机运动
8. 音频、对白、节奏和声音事件
9. 禁止事项、输出和失败条件

必须同时遵守 `REFERENCE_BINDING_TRUTH`：内部 VB01/Camera/Lighting 等只有真正被平台绑定时才能靠 @ID 执行，否则展开当前 Shot 的已批准执行信息。
