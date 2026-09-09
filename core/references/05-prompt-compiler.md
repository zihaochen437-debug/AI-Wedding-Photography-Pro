# 统一视觉 Prompt Compiler

## 1. VISUAL_PROMPT_UNIFIED_LOGIC

所有图片和视频 Prompt 必须清晰、自然、准确、具体、可视化、可执行。内部可以复杂，模型面对文本遵循：

`INTERNAL STRUCTURE → NATURAL HIGH-DENSITY DESCRIPTION`

不要把 Schema、状态机和几十个工程标签原样扔给模型，也不能为了“短”而模糊。

## 2. 权威资产 + Delta

已 `APPROVED + FROZEN` 的资产是语义权威：资产负责“是什么”，Prompt 负责“这一轮要做什么”。

公式：

`AUTHORITATIVE ASSETS + CURRENT TASK + UNLOCKED VARIABLES + CURRENT DELTA + NECESSARY CONSTRAINTS`

已锁定 → @引用；未锁定 → 详细描述；要修改 → 只描述 Delta；没有必要的禁止项 → 不写。

## 3. @参考职责

生成前明确每个 `@图片N / @素材N / @视频N / @音频N` 控制什么、不得继承什么。禁止“综合参考所有图片/融合全部人物特征”。

正常 Photo Shot：新娘当前 Look 原子资产 + 新郎当前 Look 原子资产 + 当前 Scene 原子资产 + 必要 Pose/Prop。

## 4. ACTIVE_GENERATION_REFERENCES 与 QC_AND_AUDIT_REFERENCES

真正送模型的参考与 QC/审计参考分离。QC 可以读取 AB01–AB03、原始参考和历史批准资产，但不等于模型输入必须全部包含它们。

## 5. 没有对应资产时的详细描述

根据任务写清：形状、尺寸/比例、颜色、材质、位置、左右、前后、高低、远近、身体/头部方向、接触关系、光源、光向、光质、色温、阴影、前中后景、景别、构图、Camera、透视、景深。

有真实数据用真实数据；没有时使用合理范围/相对关系，不制造 4.372m、27.38° 之类伪精确。

## 6. 抽象词

“高级、浪漫、唯美、电影感、梦幻、大片感”只能辅助，不能替代空间、材质、光、位置、动作和 Camera 描述。

## 7. 图片自然语言顺序

任务/成片目标 → @职责 → 未锁定主体/动作/空间 → Camera/景别/构图 → 光线 → 色彩/材质/环境 → 必要约束 → 真实商业摄影完成度。

## 8. 视频自然语言顺序

任务/类型/时长/比例 → @职责 → 起始画面 → 连续时间段 → 人物动作与情绪 → Camera Movement → Scene/环境变化 → 声音事件 → 收束 → 必要约束。

## 9. 已冻结分镜/Camera/Motion

有 `@STORYBOARD / @CAMERA / @LIGHTING / @MOTION / @VB01` 时不重新解释整套设计；只写严格执行及本轮 Delta。
