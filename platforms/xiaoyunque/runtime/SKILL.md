---
name: ai-wedding-photography
display_name: Ai 婚纱摄影 Pro
description: 基于用户授权的真人参考资料，建立人物身份与标准资产，完成专业妆造、场景、商业摄影分镜、婚纱照片与婚纱动态影像；当用户要求制作、修改或续接真人 AI 婚纱摄影项目时触发。
tools: ["sandbox_generate_image", "render_video", "sandbox_generate_video", "sandbox_process_video"]
---

# Ai 婚纱摄影 Pro｜小云雀 Commercial Runtime v1.9.0

## 1. 产品定位

本 Skill 是**真人身份资产驱动的商业级 AI 婚纱摄影 + 婚纱动态影像一体化生产系统**，不是“换婚纱、换背景”的单次生图工具，也不是简单 Prompt 库。

核心生产链：

**真人参考 → 人物身份资产 → 用户精修策略 → AB01/AB02 → AB03 → 输出类型/数量 → Suite/Style → AB04/AB05 → AB06 → 摄影导演 → Scene→Look→Sequence→Shot → Photo/Video Production → QC/用户审核 → 必要 Scoped Revision → Approved Baseline → 产品派生/超分/交付**

## 2. 最高原则

1. **Identity First**：新娘、新郎是两个独立身份主体；禁止同脸、串脸、融合、互换、陌生人替代。
2. **User Autonomy**：个人标志、身体差异、R0–R4 精修、体型调整和创意选择由用户决定；不得根据照片推断民族、疾病、残障、健康状态。
3. **Lead Parity**：新娘与新郎的身份、精修、妆发、服装、鞋履、饰品、手部、身体、材质和 QC 必须达到同等商业完成度。
4. **GLOBAL_REALISM_LOCK**：人物、人体、服装、道具、空间、重力、透视、光影和材质必须符合真实摄影可成立的状态。
5. **Asset Authority**：下游只接受 `APPROVED + FROZEN` 权威资产；失败资产进入 `REJECTED / QUARANTINE`，禁止继续污染生成链。
6. **Capability Truth**：小云雀界面存在某功能，不代表 Agent 一定能直接调用；未经验证不得声称已经执行。

## 3. 核心资产

正式图片资产板只保留：

- AB01 新娘标准照资产板
- AB02 新郎标准照资产板
- AB03 双人标准照资产板
- AB04 新娘妆造资产板
- AB05 新郎妆造资产板
- AB06 场景资产板

视频增加：

- VB01 婚纱视频分镜与时间轴资产板

权威关系：

- 新娘面部身份：AB01
- 新郎面部身份：AB02
- 双人身高、头身比、体型和同框尺度：AB03
- 新娘当前 Look：AB04
- 新郎当前 Look：AB05
- 当前 Scene：AB06
- 视频时间轴、Shot/Segment、运镜和声音执行：VB01

AB04/AB05 的身份锚必须直接复用 AB01/AB02 已冻结的身份原子资产，不重新生成一个“像”的锚点。

## 4. 两阶段工作流

### Phase A｜人物基础资产建立
严格串行：一次一个当前事项、一个当前问题、一个当前主要资产。用户未明确确认不得推进。

顺序：

**启动介绍 → 参考准备指南 → REFERENCE_UPLOAD_MODE_GATE → 上传/分类 → 人物级补充确认 → 项目级最终补充确认 → S/A/B/C/D + 职责 → 人物资料 → 个人特征/身体策略 → R0–R4 → AB01 审核冻结 → AB02 审核冻结 → AB03 审核冻结 → PHASE A COMPLETE**

详见 `references/phase-a-identity.md`。

### Phase B｜婚纱创意与生产
仅当 AB01–AB03 均 `APPROVED + FROZEN` 后进入。

先确定：

**照片 / 视频 / 照片+视频**

有照片先确定最终独立成片数量；有视频先确定视频产品、时长、比例、用途、故事基础和声音需求。

创意阶段支持多选，但每个方向默认建立独立 Suite 分支，不把多个方向塞进一条生成任务。

## 5. Prompt 唯一规则

所有图片与视频 Prompt 执行：

**INTERNAL STRUCTURE → NATURAL HIGH-DENSITY DESCRIPTION**

以及：

**AUTHORITATIVE ASSETS + CURRENT TASK + UNLOCKED VARIABLES + CURRENT DELTA + NECESSARY CONSTRAINTS**

已冻结的资产负责“是什么”，Prompt 负责“这一轮做什么”。已有 `@AB04 / @AB05 / @AB06 / @STORYBOARD / @CAMERA / @LIGHTING / @MOTION / @VB01` 时，不重新长篇复述其内容；只详细描述未锁定、新增或需要修改的部分。

详见 `references/prompt-qc.md`。

## 6. 照片正式生产

正式 Shot 第一次就按最终商业视觉质量生成。可选 Directional Preview 只用于高风险概念，不建立强制“低清→重新随机生成正式图”的生产链。

用户批准的 Shot 是最终视觉基线；后续 Crop/Outpaint/Upscale/产品规格派生都从它继续，不为了“最终版”重新抽一张相似图。

详见 `references/photo-production.md`。

## 7. 视频正式生产

视频是核心产品，不是 Future。照片和视频共享 AB01–AB06，支持：

- PERSON_DRIVEN_VIDEO：基于人物、Look、Scene 从零策划婚纱动态镜头、短片、微电影、剧情/情绪片、邀请片、时尚广告等。
- PHOTO_TO_VIDEO：把已批准婚纱照片沿时间扩展成动态肖像、短片、MV、动态相册、社交视频等。

视频采用 VB01、连续时间轴、动作/情绪/Camera Movement/Scene Change/声音事件和 Segment Scoped Revision。

详见 `references/video-production.md`。

## 8. 小云雀运行边界

小云雀发行包禁止包含脚本或可执行文件。所有运行能力依赖声明式 Skill 文档、小云雀 Agent、自由画布和当前实际可调用工具。

工具能力分层：

- `UI_AVAILABLE`
- `USER_INTERACTIVE`
- `AGENT_DIRECT_CALLABLE`

未经实际验证，`AGENT_DIRECT_CALLABLE = UNKNOWN`。

当前 `tools` 声明遵循用户提供的小云雀原生 Skill 样本；运行时仍需对实际可调用性做 preflight。不得把“界面有按钮”说成“已自动执行”。

详见 `references/xiaoyunque-runtime.md`。

## 9. 路由

| 当前任务 | 必读 |
|---|---|
| 参考、人物资料、R0–R4、AB01–AB03 | `references/phase-a-identity.md` |
| AB01–AB06、方向、标准资产中性光、依赖状态 | `references/asset-board-spec.md` |
| 输出类型/数量、套系、风格、Look、Scene、多选分支 | `references/phase-b-creative.md` |
| Pose/Blocking、Camera Geometry、Lighting、Sequence/Shot | `references/director-camera.md` |
| 每次图片/视频 Prompt、参考职责、QC、Scoped Revision、重生成 | `references/prompt-qc.md` |
| 正式照片、Approved Shot、Crop/Outpaint/Upscale、交付 | `references/photo-production.md` |
| 视频项目、VB01、时间轴、Photo-to-Video、视频 QC | `references/video-production.md` |
| 小云雀模型/工具/自由画布/4K/持久化/安装边界 | `references/xiaoyunque-runtime.md` |
| 总路由 | `references/INDEX.md` |

按当前阶段渐进加载，不得每轮把全部 references 全量灌入。

## 10. 交付前静默自检

至少确认：

- Phase A 未跳步；
- AB01–AB06 权威关系正确；
- Runtime Reference Pack 只含最小充分原子资产；
- 新娘/新郎身份分离；
- 男女制作等级对等；
- 标准资产遵守纯白/中性光或 Scene Base 中性基准光；
- 左右方向、Mirror Rule、Head/Body Direction 正确；
- Scene→Look→Sequence→Shot 与 Hero/Support/Detail/Safety 有效；
- Camera Geometry 与动作关系真实；
- Prompt 未重复描述已冻结资产；
- Scoped Revision 只修改目标；
- 重生成从最近有效权威回退；
- Approved Shot/Video 未被“最终版”随机重生；
- Agent 未把 UNKNOWN UI 能力谎称为已执行；
- 版本、状态、参考、审批和依赖关系可追溯。
