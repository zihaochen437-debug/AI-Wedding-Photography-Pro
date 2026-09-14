# Ai 婚纱影像 Pro v2｜小云雀婚纱影视正式生产

婚纱影视是核心产品，不是 Future。所有类型共享同一真人身份根，不建立“视频版新娘/新郎”。

## 1. WEDDING_FILM_PRODUCT_CLASS

### VF01｜动态婚纱影像

以 Approved Wedding Photo 为视觉母体，把静态照片导演成具有时间、动作、微表演、镜头运动和同期声的动态叙事。照片中的身份、Look、Scene、构图和关键道具默认锁定。

### VF02｜创意叙事婚纱影视

从人物九图身份标准出发，根据用户真实故事、用户创意或预制故事母型重新建立剧情 Character State、Story Look、Wardrobe、Makeup、Props、Film Scene、表演、Camera 和声音。

### VF03｜混合叙事婚纱短片

同时管理情侣故事线和婚纱影像线，通过动作、道具、声音、视觉母题、构图、光线或时空关系融合；婚纱部分必须成为故事结果，而不是简单插播。

底层 `PHOTO_DERIVED_VIDEO` 与 `ASSET_DRIVEN_FILM` 只是生成路线，不取代 VF01/VF02/VF03 产品分类。

## 2. FINAL MASTER 时长

最终成片最长 `<= 5:00`。这是成片时长，不是单次模型时长。

长片必须拆成：`FILM → ACT/CHAPTER → SEQUENCE → SCENE → SHOT → TAKE`，通过多段生成、Take 选择、Scoped Revision 和剪辑组成。

不得因为 Seedance 当前某模式支持更长生成，就默认把整部影片交给一个长 Prompt。

## 3. VIDEO_PROJECT_GATE

确认：VF01/VF02/VF03、最终时长、横/竖与画幅、用途/发布平台、故事来源、真实/改编/虚构边界、动态强度、是否有 Scene Dialogue、是否规划 VO、最终音乐方向、Scene 数、Look 数及用户禁区。

背景音乐方向可以在策划中记录，但在 Picture Lock 前不得生成或混入正式 Shot。

## 4. PROFESSIONAL FILM PRODUCTION

按专业职责执行：策划 → 编剧 → Script Breakdown → 导演 → 表演指导 → 摄影指导 → 美术/服化道/道具 → Continuity → Storyboard/Previz → Shot Production → Take → Editing → Sound → Color → QC → Master。

这些是专业职责，不要求小云雀运行 14 个独立 Agent。

## 5. 逻辑影视资产

- VP01｜Video Production Brief
- VS01｜Story & Beat Sheet
- VD01｜Director Treatment
- VC01｜Video Continuity Bible
- VB01｜Video Storyboard + Timeline Master
- VSL01｜Shot List
- VA01｜Audio Bible
- EDL01｜Edit Decision List

除 VB01/Keyframe 等必要视觉材料外，大多数是结构化执行资产，不额外增加人物身份图片槽位。

## 6. STORY_APPROVAL_GATE / STORYBOARD_APPROVAL_GATE

故事与分镜是两个独立审批门。

默认：

`STORY_AUTONOMY = FALSE`
`STORYBOARD_AUTONOMY = FALSE`

只有用户明确说“故事由 Skill 自行设计”或“分镜由 Skill 自行设计”，对应字段才改为 TRUE。Phase B 的 Ai自动/自动模式不自动取得这两个权限。

VF02/VF03：Story Concept / Logline / Synopsis / Beat Sheet / Ending 先确认，再进入正式 Screenplay 和 VB01。

VF01：有明显叙事时先确认动态叙事方案，再确认 VB01。

Story V2 替换 Story V1 时，旧 VB01 → `STALE`，相关 Shot → `REVALIDATION_REQUIRED`。只修改某一 Shot 时使用 Scoped Revision，不重写整部 Story。

## 7. SCRIPT_BREAKDOWN_ENGINE

VF02/VF03 Approved Script 拆解：角色、角色状态、Story Look、服装、妆发、道具、Scene、Set Dressing、车辆、VFX、对白、同期声、特殊设备、Reference Needs、Risk Elements。

预设资产包括但不限于示例；剧本需要的新服装、道具和 Scene 可以动态创建，经用户审核后进入项目资产台账。

## 8. 0.1 秒时间体系

`PLANNING_TIMELINE_PRECISION = 0.1s`：VB01、Shot Card、Sound Event、EDL、QC 都记录到 0.1 秒。

但小云雀/Seedance 实际生成控制必须执行 `MODEL_TIMING_ADAPTER`：

- 0.1 秒是导演计划和后期数据精度；
- Prompt 中的时间窗口按当前目标模型真正支持且稳定的粒度编译；
- 不宣称视频模型拥有未验证的 0.1 秒动作触发精度；
- 最终剪辑点执行 `FRAME_SNAP_POLICY`，吸附实际帧边界。

## 9. VB01

至少包含：Video ID、版本、VF 产品、最终时长、画幅、Story/Storyboard 审批状态、Act、Sequence、Scene、Shot、Source Line、0.1s 起止时间、Story Purpose、人物状态、Look、Prop、Opening State、End State、Blocking、Action、Performance、Shot Scale、Composition、Camera、Camera Motion、Focus、Lighting、Sync Sound、Dialogue、Transition、Continuity、Reference Binding、Status。

VF01 增加 `SOURCE_PHOTO_ID / PHOTO_FIDELITY_LOCK / ALLOWED_MOTION`。
VF02 增加 `STORY_BEAT_ID / CHARACTER_MOTIVATION / DIALOGUE_OBJECTIVE / STORY_PROP_STATE`。
VF03 增加 `SOURCE_LINE=STORY/WEDDING/BRIDGE / BRIDGE_TYPE / VISUAL_MOTIF / AUDIO_MOTIF`。

VB01 批准后 `APPROVED + FROZEN`，未经批准不得开始正式 Shot Production，除非 `STORYBOARD_AUTONOMY=TRUE`。

## 10. VIDEO_SHOT_CONTROL_CARD

每个 Shot 至少管理：

`SHOT_ID / TAKE_ID / START / END / DURATION / PURPOSE / FIRST_FRAME_CONTRACT / BRIDE-GROOM POSITION / BODY_DIRECTION / HEAD_DIRECTION / GAZE / DISTANCE / WEIGHT / HAND_ACTION / CONTACT / EXPRESSION / PERFORMANCE_BEAT / ACTION_PHASE / PROP_STATE / CAMERA_START-END-PATH / SHOT_SCALE / FOCUS / LIGHTING / SYNC_SOUND / TRANSITION / END_STATE_CONTRACT / QC_RISK`

上一 Shot 的 End State 是下一 Shot 的连续性输入。

## 11. 表演指导

采用已研究的 ACTING 方法，但婚纱化处理：表演写可观察行为，不直接让人物“演浪漫/演难过”。叙事场景按需要使用 Objective / Obstacle / Tactic / Beat / Subtext / Listening / Reaction / Eye Life / Breath / Business / Proxemics / Status。

VF01、安静婚纱肖像、纯视觉诗不强制制造冲突或“谁失败”；只要求注意力、关系、动作和微表演真实。

通用规则：眼睛通常先于头部到达目标；听者在对方说话过程中产生反应；重要信息后允许 Assessment Beat；强事件状态跨镜具有惯性；双人反应避免机械同步。

## 12. Blocking / Camera / Physics

先 Blocking，后 Framing：先人物目标、站位、路线、距离、道具和接触，再决定 Camera。

Camera Motion 必须有动机；没有动机优先不动。记录起止位置、轨迹、速度、加减速、目标、稳定方式、Focus 与动机。

人体、步态、脚地接触、裙摆、头纱、发丝、宠物、道具、风、水等执行真实重力、质量、惯性、摩擦、接触和 Follow-through，禁止漂浮、滑行、穿模、无重量布料和随机 Camera 漂移。

## 13. Continuity

根据 Shot/Scene 需要检查：180°轴、Camera Side、Eyeline、Match on Action、Screen Direction、Spatial/Temporal Continuity、Prop、Look/Wardrobe、Lighting/Color、Emotion/Performance、Audio Continuity。

VF03 Story/Wedding 切换必须有 Bridge 原因：Match on Action / Prop / Color / Motion / Graphic / Audio Bridge 等，不随机切时空。

## 14. 小云雀模型路由

模型使用始终受 `RUNTIME_CAPABILITY_TRUTH_POLICY` 约束：官方存在 ≠ 当前账号可调用。

### VIDEO_SHOT / VIDEO_SEQUENCE

优先候选：**Seedance 2.5**，用于正式 Shot、连续 Sequence、多人物表演、复杂运镜与参考式视频；但每次生产前确认当前小云雀实际可用性。

### SECONDARY VIDEO

**Seedance 2.0**：多模态参考、特定任务或 2.5 当前入口不可用时的备用。

**Seedance 2.0 Fast / Mini**：若当前 Runtime 可用，优先用于低成本 Previz、动作/构图/节奏测试，不自动作为最终商业母片。

**Seedance 1.5 Pro / 1.x**：只在当前运行环境和具体对白/兼容任务表现有证据时路由，不因版本名称自动优先。

### IMAGE / KEYFRAME

角色状态、Story Look、Prop、Scene、Storyboard、Opening/Ending Frame、Bridge Keyframe 由当前小云雀实际可用的最高稳定图片/编辑模型承担。Seedream/Anycook/旗舰生图等按 Runtime 能力卡选择，不写死单一图片模型。

### 3D导演台

若当前自由画布真实可用，用于 Scene Blockout、人物 Blocking、Camera Station/Path、空间预演；不得编造未实测的坐标/骨骼/API 参数。

### AUDIO

Seed Audio 等音频模型只有在当前小云雀直接可调用能力被验证后才进入自动路由；否则保留 VA01 和后期声音方案，由用户/平台可用工具执行。

## 15. 生成策略

按导演目标选择：

- `SHOT_BASED`：高控制 Hero、面部、关键表演；
- `SEQUENCE_ONE_TAKE`：适合连续动作与连续 Camera；
- `HYBRID`：商业默认候选，环境/互动 Sequence/Hero/Ending 按各自控制需求生产。

模型上限不是镜头设计目标。复杂运动、多人物接触、裙摆/头纱/宠物等高物理风险 Shot 应优先缩短或拆分，并通过 Take/QC 管理。

## 16. TAKE / VIDEO_SCOPED_REVISION

允许有限目的性 Take：`TAKE-A / TAKE-B / SAFETY → SELECTED TAKE`。先导演再生成，不无上限抽卡。

局部问题只开放目标时间段和目标域。例如 7.0–11.0 秒新娘面部错误，只修这一段新娘面部；冻结其他时间、新郎、Look、Scene、动作、Camera、Audio、Duration，除非目标本身要求联动。

Approved Video 是视觉基线；后续片段编辑、延长、拼接、超分、声音和输出不默认重生整条。

## 17. NO_BGM_BEFORE_PICTURE_LOCK

这是 P0。

策划、剧本、Storyboard、Previz、Shot Generation、Take Selection、Scoped Revision、Assembly、Rough Cut、Fine Cut 阶段：**禁止生成或混入非剧情来源背景音乐。**

Shot 生产只允许 `SYNC_SOUND_ONLY`：现场对白/誓言、呼吸/自然笑声、Ambience、Foley、剧情内真实声源和有意 Silence。

默认 `VOICEOVER_POST_ONLY`：VO 可以在前期写好并规划时间，但不在 Shot Generation 中混入，后期声音阶段再加入。

唯一音乐例外：剧情中真实存在、人物可听见的 `DIEGETIC / PLAYBACK MUSIC`，必须提前登记。

正式素材出现未经要求的 BGM：`AUDIO_QC_FAIL`，移除或重新生成对应音频/片段。

## 18. EDITING / AUDIO POST / COLOR

`Take Selection → Assembly Cut → Rough Cut → Narrative/Continuity Review → Fine Cut → PICTURE_LOCK → Dialogue Edit → ADR if needed → Foley → Ambience → Sound Design → VO → Music Spotting → Music → Mix → Color Grade → VFX/Cleanup → Final QC → Master`

只有 `PICTURE_LOCK` 后背景音乐进入完整影片。

EDL01 记录 Shot、Selected Take、Source In/Out、Timeline In/Out、前后镜、Cut、Audio Cut、Transition、Notes。显示精度 0.1s，实际切点吸附帧边界。

## 19. VIDEO QC

检查身份、逐帧脸、身高体型、手、Look、服装、妆发、道具、Scene、Lighting/Color、Physics/Motion、Camera/Focus、Screen Direction、Eyeline、Action Match、Flicker/Morphing、群演复制、AV Sync、Lip Sync（适用）、Dialogue、Ambience/Foley、未经授权 BGM 与整体叙事节奏。

硬失败进入 `REJECTED / QUARANTINE`。

## 20. Master 与平台派生

最终 16:9 / 9:16 / 1:1 等平台版本必须重新 Reframe 并 QC，不允许盲裁破坏人物、道具、视线和剧情信息。

## 21. Runtime Contract

只有实际工具调用成功时才能声称生成/处理完成。工具/模型不可用时，仍可输出 VP01/VS01/VD01/VC01/VB01/VSL01/VA01/EDL、Prompt、参考绑定和用户可执行步骤，但不得假装已经生成。
