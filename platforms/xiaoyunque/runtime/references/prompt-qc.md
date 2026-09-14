# v2 统一 Prompt Compiler、参考权威、QC 与修订

## 1. VISUAL_PROMPT_UNIFIED_LOGIC

所有照片、资产、分镜和视频 Prompt 必须清晰、自然、准确、具体、可视化、可执行。

内部可以复杂；模型面对文本遵循：

`INTERNAL STRUCTURE → RESOLVE → TASK FILTER → NATURAL HIGH-DENSITY DESCRIPTION`

不把 Schema、状态机和工程标签原样扔给模型，也不能为了短而模糊。

## 2. 先解析，再编译

`USER CHOICE / APPROVED PLAN → PROFILE RESOLVER → USER OVERRIDES → ASSET AUTHORITY → CURRENT TASK FILTER → MODEL/PLATFORM ADAPTER → NATURAL LANGUAGE COMPILER`

至少支持：`RETOUCH_PROFILE_RESOLVER / LOOK_PROFILE_RESOLVER / MAKEUP_PROFILE_RESOLVER / DIRECTOR-CAMERA-LIGHTING-MOTION RESOLVER`。

“R2 商业自然级”“法式清透”“电影感”“导演模式”等 UI/内部名称都不能单独作为正式生成指令。

## 3. Asset Authority + Delta

已 `APPROVED + FROZEN` 的资产负责“是什么”，Prompt 负责“这一轮做什么”。

公式：

`AUTHORITATIVE ASSETS + CURRENT TASK + UNLOCKED VARIABLES + CURRENT DELTA + NECESSARY CONSTRAINTS`

- 已锁定且真实绑定给模型 → 参考承担主要语义；
- 未锁定 → 详细描述；
- 要修改 → 只描述 Delta；
- 没变化 → 不重新策划；
- 没必要的禁止项 → 不写。

## 4. REFERENCE_BINDING_TRUTH

内部资产名不是模型天然认识的控制参数。

只有当小云雀当前工具真实把对应图片、视频、音频或结构化参考传给目标模型时，`@AB01 / @AB04 / @STORYBOARD / @CAMERA / @VB01` 等引用才算执行引用。

若当前工具不能直接绑定内部资产对象：

1. 继续以该 `APPROVED + FROZEN` 资产为设计权威；
2. 提取当前任务需要的已批准可见状态；
3. 转成自然语言或实际可上传的最小参考素材；
4. 不得只发送一个内部 Asset ID 并假设模型理解。

原则：**禁止重复策划，不等于禁止展开执行信息。**

## 5. @参考职责

每个 `@图片N / @素材N / @视频N / @音频N` 必须说明控制什么、不得继承什么。

禁止：

- “综合参考所有图片”
- “融合所有人物特征”
- 动作视频继承演员身份/服装/Scene
- Scene 参考覆盖人物身份

正常 Photo Shot：新娘当前 Look + 新郎当前 Look + 当前 Scene + 当前 Shot 真正需要的 Pose/Prop/Control Asset。

## 6. ACTIVE_GENERATION_REFERENCES 与 QC_AND_AUDIT_REFERENCES

真正送模型的参考与 QC/审计参考分离。

QC 可以读取人物九图、原始参考和历史批准资产，但不等于生成模型必须全部吃进去。

身份升级链按最小充分原则：当前 Look → 对应 M01/U/F/D → 必要时 AB03-C01 → 一张最佳原始真人证据。增加更高权威参考时替换冗余低权威参考，不无限叠加。

## 7. RETOUCH 编译

R0–R4 必须展开成当前任务相关的具体域：

`skin / face_geometry / eyes / brows / nose / lips_teeth / hair_beard / neck_shoulders / hands / body_posture / body_contour / personal_signatures / forbidden_changes`

上半身板只编译上半身相关域；细节板按区域调用对应 profile。不得向所有任务复制无关的全身精修说明。

## 8. LOOK / MAKEUP 编译

AB04/AB05 生成前把 Look 名称展开为可见状态。新娘妆面至少包含：

`base_and_complexion / skin_finish / brows / eyeshadow / eyeliner / lashes / under_eye / blush / contour / highlight / lips / intensity / texture_retention`

Look Prompt 同时满足：身份锚清楚、妆面存在、服装/发型/饰品明确、个人标志正确、禁止未经授权的五官/年龄/体型重设计。

## 9. 没有权威资产时的详细描述

根据任务写清：形状、尺寸/比例、颜色、材质、位置、左右、前后、高低、远近、身体/头部方向、接触关系、光源、光向、光质、色温、阴影、前中后景、景别、构图、Camera、透视、景深。

有真实数据用真实数据；没有时用合理范围/相对关系，不制造伪精确。

抽象词“高级、浪漫、唯美、电影感、梦幻、大片感”只能辅助，不能替代可见现实。

## 10. Prompt 密度

`PRECISION > VERBOSITY`。高密度信息优先用于身份、当前动作、空间、相机、光线、时间、声音和当前风险；参考已经明确的内容由参考承担。

## 11. 图片自然语言顺序

任务/成片目标 → 参考职责 → 当前身份/Look 绑定 → 未锁定主体/动作/空间 → Camera/景别/构图 → 光线 → 色彩/材质/环境 → 当前必要风险约束 → 真实商业摄影完成度。

## 12. 视频自然语言顺序

任务/类型/时长/比例 → 参考职责 → 起始状态 → 连续时间轴 → 人物表演/动作 → Camera Movement → Scene/环境变化 → 同期声音事件 → End State → 当前必要风险约束。

视频对外 Prompt 继续使用九块结构：当前任务；类型/时长/画幅；参考职责；人物身份/妆造/比例；Scene；连续时间轴；表演/动作/Camera；音频/对白/声音事件；禁止/输出/失败条件。

## 13. 已冻结 Storyboard / Camera / Lighting / Motion

有真实可执行绑定时，不重新设计整套方案，只写当前 Delta。

若只是内部已批准资产而小云雀没有直接绑定能力，则调用 `REFERENCE_BINDING_TRUTH` 展开当前 Shot 所需的已批准执行状态。

## 14. RISK_AWARE_NEGATIVE_COMPILER

默认先写正确状态，再对当前 Shot 最可能发生的失败使用少量局部禁止项。禁止每个 Prompt 无差别追加巨大 Negative List。

## 15. 硬失败与一致性域

硬失败包括：人物不像本人、同脸/串脸/交换、明显身高/体型漂移、严重手部/人体错误、婚纱/礼服无授权改款、关键饰品错误、Scene 固定结构漂移、AI 塑料皮肤、群演继承主角脸、Revision 越界、Upscale 重绘人物、视频逐帧变脸/Morphing、严重运镜/音画错误、首版新娘 Look 未执行用户已确认妆容。

至少检查：身份/面部、人体结构、服装结构、妆发饰品、道具/接触、姿势/站位、Scene、Camera/Lighting/Color、时间连续性（视频）。失败进入 `REJECTED / QUARANTINE`。

## 16. Scoped Revision

修改什么只开放什么 + 必要最小连接区域；其他已批准域冻结。

例：只修新娘眼妆时，只开放眼影、眼线、睫毛和必要边缘；锁定脸型、鼻唇、新郎、发型、婚纱、Scene、Camera、Lighting 与已经正确肤质。越界为 `REVISION_SCOPE_VIOLATION`。

## 17. 重生成

`REGENERATION_FOLLOWS_ASSET_AUTHORITY`：重新生成不等于重新策划。继承仍有效权威资产、Storyboard/Camera/Lighting，仅加入失败原因和 Delta。

若正在重做的资产已 `REJECTED / QUARANTINE`，不得继续作为最高权威；执行 `REGENERATE_FROM_NEAREST_VALID_AUTHORITY` 回退到最近有效上游。