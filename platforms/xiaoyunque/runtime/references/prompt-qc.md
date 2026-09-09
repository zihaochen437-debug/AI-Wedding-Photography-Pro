# 统一 Prompt Compiler、参考权威、QC 与修订

## 1. VISUAL_PROMPT_UNIFIED_LOGIC

所有照片、资产、分镜和视频 Prompt 必须：

清晰、自然、准确、具体、可视化、可执行。

内部可以复杂；模型面对文本遵循：

`INTERNAL STRUCTURE → NATURAL HIGH-DENSITY DESCRIPTION`

不把 Schema、状态机和工程标签原样扔给模型，也不能为了短而模糊。

## 2. Asset Authority + Delta

已 `APPROVED + FROZEN` 的资产负责“是什么”，Prompt 负责“这一轮做什么”。

公式：

`AUTHORITATIVE ASSETS + CURRENT TASK + UNLOCKED VARIABLES + CURRENT DELTA + NECESSARY CONSTRAINTS`

- 已锁定 → @引用
- 未锁定 → 详细描述
- 要修改 → 只描述 Delta
- 没变化 → 不重新解释
- 没必要的禁止项 → 不写

## 3. @参考职责

每个 `@图片N / @素材N / @视频N / @音频N` 必须说明控制什么、不得继承什么。

禁止：

“综合参考所有图片”
“融合所有人物特征”

正常 Photo Shot：

新娘当前 Look 原子资产 + 新郎当前 Look 原子资产 + 当前 Scene 原子资产 + 必要 Pose/Prop。

## 4. ACTIVE_GENERATION_REFERENCES 与 QC_AND_AUDIT_REFERENCES

真正送模型的参考与 QC/审计参考分离。

QC 可以读取 AB01–AB03、原始参考和历史批准资产，但不等于生成模型必须全部吃进去。

身份升级链：

- 正常：AB04 + AB05 + AB06
- 新娘漂移：+ AB01
- 新郎漂移：+ AB02
- 比例错误：+ AB03
- 方向持续失败：+ 对应人物该方向 1 张最佳真人原图
- 多个 Shot 持续漂移：重建对应 AB04/AB05

增加更高权威参考时，应替换冗余低权威参考，不无限叠加。

## 5. 没有权威资产时的详细描述

根据任务写清：

形状、尺寸/比例、颜色、材质、位置、左右、前后、高低、远近、身体/头部方向、接触关系、光源、光向、光质、色温、阴影、前中后景、景别、构图、Camera、透视、景深。

有真实数据用真实数据；没有时用合理范围/相对关系，不制造伪精确。

抽象词“高级、浪漫、唯美、电影感、梦幻、大片感”只能辅助，不能替代可见现实。

## 6. 图片自然语言顺序

任务/成片目标 → @职责 → 未锁定主体/动作/空间 → Camera/景别/构图 → 光线 → 色彩/材质/环境 → 必要约束 → 真实商业摄影完成度。

## 7. 视频自然语言顺序

任务/类型/时长/比例 → @职责 → 起始画面 → 连续时间段 → 人物动作与情绪 → Camera Movement → Scene/环境变化 → 声音事件 → 收束 → 必要约束。

## 8. 已冻结 Storyboard / Camera / Lighting / Motion

有 `@STORYBOARD / @CAMERA / @LIGHTING / @MOTION / @VB01` 时不重新解释整套设计；只写严格执行及本轮 Delta。

## 9. 硬失败与一致性域

硬失败包括：人物不像本人、同脸/串脸/交换、明显身高/体型漂移、严重手部/人体错误、婚纱/礼服无授权改款、关键饰品错误、Scene 固定结构漂移、AI 塑料皮肤、群演继承主角脸、Revision 越界、Upscale 重绘人物、视频逐帧变脸/Morphing、严重运镜/音画错误。

至少检查九大域：

身份/面部、人体结构、服装结构、妆发饰品、道具/接触、姿势/站位、Scene、Camera/Lighting/Color、时间连续性（视频）。

失败进入 `REJECTED / QUARANTINE`。

## 10. Scoped Revision

修改什么只开放什么 + 必要最小连接区域；其他已批准域冻结。

例：只修新娘右手时，锁定新娘脸、新郎、身高体型、站位动作、另一只手、婚纱、礼服、Scene、Camera、Composition、Lighting、Color。

越界为 `REVISION_SCOPE_VIOLATION`。

## 11. 重生成

`REGENERATION_FOLLOWS_ASSET_AUTHORITY`：重新生成不等于重新策划。继承仍有效的权威资产、Storyboard/Camera/Lighting，仅加入失败原因和 Delta。

若正在重做的资产已 `REJECTED / QUARANTINE`，不得继续作为最高权威；执行 `REGENERATE_FROM_NEAREST_VALID_AUTHORITY` 回退到最近有效上游。
