# v2 统一视觉 Prompt Compiler

## 1. VISUAL_PROMPT_UNIFIED_LOGIC

所有图片和视频 Prompt 必须清晰、自然、准确、具体、可视化、可执行。内部可以复杂，模型面对文本遵循：

`INTERNAL STRUCTURE → RESOLVE → TASK FILTER → NATURAL HIGH-DENSITY DESCRIPTION`

不要把 Schema、状态机和几十个工程标签原样扔给模型，也不能为了“短”而模糊。

## 2. 先解析，再编译

任何 UI 名称、预设名、导演标签都不是最终生产指令。至少经过：

`USER CHOICE / APPROVED PLAN → PROFILE RESOLVER → USER OVERRIDES → ASSET AUTHORITY → CURRENT TASK FILTER → MODEL/PLATFORM ADAPTER → NATURAL LANGUAGE COMPILER`

典型 Resolver：

- `RETOUCH_PROFILE_RESOLVER`
- `LOOK_PROFILE_RESOLVER`
- `MAKEUP_PROFILE_RESOLVER`
- `DIRECTOR / CAMERA / LIGHTING / MOTION RESOLVER`

禁止把“R2 商业自然级”“法式清透”“电影感”“DIR01-D03”等内部名称直接当作足够 Prompt。

## 3. Asset Authority + Delta

已 `APPROVED + FROZEN` 的资产负责“是什么”，Prompt 负责“这一轮做什么”。

公式：

`AUTHORITATIVE ASSETS + CURRENT TASK + UNLOCKED VARIABLES + CURRENT DELTA + NECESSARY CONSTRAINTS`

- 已锁定且已真实绑定给模型 → 以参考资产承担主要语义，不重复重新设计；
- 未锁定 → 详细描述；
- 要修改 → 只描述 Delta；
- 没变化 → 不重新策划；
- 没必要的禁止项 → 不写。

## 4. REFERENCE_BINDING_TRUTH

内部资产名不是模型天然认识的控制参数。

只有当当前平台/工具真正把对应图片、视频、音频或结构化参考传给目标模型时，`@AB01 / @AB04 / @STORYBOARD / @CAMERA / @VB01` 等引用才可以被视为“执行引用”。

如果当前运行时不能把内部资产对象直接绑定给目标模型：

1. 仍以该 `APPROVED + FROZEN` 资产为设计权威；
2. 从中提取当前任务真正需要的已批准可见状态；
3. 将其展开成自然语言或可上传的最小参考素材；
4. 不得把一个仅供内部管理的 Asset ID 单独发送给模型并假设模型理解。

原则：**禁止重复策划，不等于禁止展开执行信息。**

## 5. @参考职责

生成前明确每个 `@图片N / @素材N / @视频N / @音频N` 控制什么、不得继承什么。禁止：

- “综合参考所有图片”
- “融合全部人物特征”
- 让动作参考视频继承演员身份/服装/Scene
- 让 Scene 参考覆盖人物身份

正常 Photo Shot：新娘当前 Look + 新郎当前 Look + 当前 Scene + 当前 Shot 真正需要的 Pose/Prop/Control Asset。

## 6. ACTIVE_GENERATION_REFERENCES 与 QC_AND_AUDIT_REFERENCES

真正送模型的参考与 QC/审计参考分离。QC 可以读取人物九图、原始参考和历史批准资产，但不等于模型输入必须全部包含它们。

身份升级遵循最小充分原则：当前 Look → 对应 M01/U/F/D → 必要时 AB03-C01 → 一张最佳原始真人证据。增加更高权威参考时替换冗余参考，不无限叠加。

## 7. RETOUCH 编译

正式人物资产 Prompt 必须将 R0–R4 解析为当前任务相关的具体域：

`skin / face_geometry / eyes / brows / nose / lips_teeth / hair_beard / neck_shoulders / hands / body_posture / body_contour / personal_signatures / forbidden_changes`

例如上半身板只编译上半身可见且相关的精修域；细节板按区域调用对应 profile。不得向所有任务复制一整段无关的全身精修说明。

## 8. LOOK / MAKEUP 编译

AB04/AB05 生成前把 Look 名称展开为可见状态。新娘妆面至少包含：

`base_and_complexion / skin_finish / brows / eyeshadow / eyeliner / lashes / under_eye / blush / contour / highlight / lips / intensity / texture_retention`

Look Prompt 必须同时满足：身份锚清楚、妆面存在、服装/发型/饰品明确、个人标志正确、禁止未经授权的五官/年龄/体型重设计。

## 9. 没有对应权威资产时的详细描述

根据任务写清：形状、尺寸/比例、颜色、材质、位置、左右、前后、高低、远近、身体/头部方向、接触关系、光源、光向、光质、色温、阴影、前中后景、景别、构图、Camera、透视、景深。

有真实数据用真实数据；没有时使用合理范围/相对关系，不制造伪精确。

## 10. 抽象词与密度控制

“高级、浪漫、唯美、电影感、梦幻、大片感”只能辅助，不能替代空间、材质、光、位置、动作和 Camera 描述。

`PRECISION > VERBOSITY`：Prompt 不追求机械短，也不靠堆字体现专业。高密度信息优先放在身份、当前动作、空间、相机、光线、时间、声音和当前风险上；参考已经明确的内容尽量由参考承担。

## 11. 图片自然语言顺序

任务/成片目标 → 参考职责 → 当前身份/Look 绑定 → 未锁定主体/动作/空间 → Camera/景别/构图 → 光线 → 色彩/材质/环境 → 当前必要风险约束 → 真实商业摄影完成度。

## 12. 视频自然语言顺序

任务/类型/时长/比例 → 参考职责 → 起始状态 → 连续时间轴 → 人物表演/动作 → Camera Movement → Scene/环境变化 → 同期声音事件 → End State → 当前必要风险约束。

外部视频生产 Prompt 继续保留九块执行结构：

1. 当前视频任务
2. 视频类型、时长与画幅
3. 参考素材职责映射
4. 人物身份、妆造和比例锁
5. Scene 与视觉风格
6. 连续时间轴
7. 表演、动作与摄影机运动
8. 音频、对白、节奏和声音事件
9. 禁止事项、输出和失败条件

内部 Film Production 资产可以更复杂，但最终必须编译到目标模型能够执行的语言。

## 13. 已冻结 Storyboard / Camera / Lighting / Motion

有真实可执行的 `@STORYBOARD / @CAMERA / @LIGHTING / @MOTION / @VB01` 绑定时，不重新设计整套方案，只写当前 Delta。

若只是内部已批准资产而平台没有直接绑定能力，则调用 `REFERENCE_BINDING_TRUTH`：展开当前 Shot 所需的已批准执行状态，不得重新策划。

## 14. RISK_AWARE_NEGATIVE_COMPILER

默认先写正确状态，再对当前镜头最可能发生的失败使用少量局部禁止项。禁止每个 Prompt 无差别追加巨大 Negative List。

例如：宠物 Shot 重点防重复宠物/爪耳变形；披纱 Shot 重点防披纱变额外肢体；妆面近景重点防身份美型漂移；视频生产期明确 `no background music`。