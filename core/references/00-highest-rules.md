# Ai 婚纱影像 Pro｜最高规则

## PROJECT_NAME_V2_LOCK

从 v2.0.0 起，项目正式名称统一为：**Ai 婚纱影像 Pro**。

`Ai 婚纱摄影 Pro` 仅作为 v1.x 历史名称保留，不再作为 v2+ 当前项目正式显示名称。技术仓库名、历史 tag 和兼容机器 ID 可以为兼容性继续保留旧字符串，但用户可见项目名称、v2+ 文档标题与正式产品称谓统一使用 `Ai 婚纱影像 Pro`。

## 产品定义

Ai 婚纱影像 Pro 是**真人身份资产驱动的商业级 AI 婚纱摄影 + 婚纱影视一体化生产系统**，不是单次换装/换背景工具，也不是 Prompt 模板库。

产品同时覆盖：

- 商业婚纱摄影；
- VF01 动态婚纱影像；
- VF02 创意叙事婚纱影视；
- VF03 混合叙事婚纱短片；
- 与上述产品相关的人物资产、策划、编剧、导演、摄影、灯光、表演、美术、服化道、场记、剪辑、声音、调色、QC 与商业交付。

## Identity First

- 新娘、新郎是两个独立身份主体。
- 身份高保真优先于风格、美化、场景、灯光和所谓高级感。
- 任何不能被明确识别为本人的输出都不合格。
- 禁止同脸、串脸、融合、互换、陌生人替代。
- 配角/伴郎/伴娘/宾客执行 `CAST_PORTRAIT_ISOLATION`。

## User Autonomy

用户决定精修等级、体型调整、眼镜、首饰、纹身、痣、疤痕、胡须、牙齿特征、假肢、轮椅、辅助器具及其他个人标志。不得根据照片推断民族、疾病、残障、健康状态或真实身体差异。

工作模式、故事自主权、分镜自主权是不同授权维度；任何自动模式都不得静默取得用户未授予的创意或费用决策权。

## Lead Parity

新娘和新郎获得同等级身份、精修、妆发、服装、鞋履、饰品、手部、身体、材质与 QC。不能女主详尽、男主一句“黑色高级西装”。

## GLOBAL_REALISM_LOCK

**自然**：表情、动作、头发、服装、裙摆、头纱、互动和环境符合真实世界的自然状态。

**真实**：人体结构、手部、珠宝连接、道具握持、地面接触、重力、空间、透视与光影现实可成立。

**写实**：结果像专业婚纱摄影/影视摄影，而不是模板脸、塑料皮肤、蜡像、虚假 HDR、异常锐化或 CG 人像。

## Asset Authority

下游正式权威只接受 `APPROVED + FROZEN`。失败资产进入 `REJECTED / QUARANTINE`，旧版本由 `SUPERSEDED` 追踪。

人物标准阶段执行 `STANDARD_IDENTITY_4_PLUS_1_POLICY`：新娘 4 张 + 新郎 4 张 + 双人正面全身 1 张，达到 `9/9 APPROVED + FROZEN` 才能结束 Phase A。

## Prompt Constitution

统一采用：

`AUTHORITATIVE ASSETS + CURRENT TASK + UNLOCKED VARIABLES + CURRENT DELTA + NECESSARY CONSTRAINTS`

任何 UI 名称/预设名必须先经过 Resolver。内部 Asset ID 只有在运行时真实绑定给模型时才可直接承担执行语义；否则必须从已批准资产展开当前任务需要的可见执行信息。

## 生产因果链

`Reference → Retouch/Profile → 9-image Identity Standard → Work Mode → Product Branch → Look/Story Assets → Scene/Props → Director/Blocking/Camera/Lighting → Sequence/Shot → Approved Baseline → Edit/Post → Final Master`

平台 Adapter 可以改变执行方式，但不得静默削弱上述身份、审批、资产权威、受控修订和 QC 标准。