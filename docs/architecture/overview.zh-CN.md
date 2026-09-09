# 架构总览

[English](overview.md) | [简体中文](overview.zh-CN.md)

AI Wedding Photography Pro 将**平台无关的生产语义**与**平台专项执行方式**彻底分离。

## 1. Source Archive

历史研究、实验方案、被替代规则、测试记录和旧 Runtime 继续保留，作为设计演进档案。历史资料不会自动成为当前有效行为。

## 2. Active Canon

Active Canon 是当前权威规则集合，用于裁决历史版本冲突；旧规则应明确标记为 `SUPERSEDED`，不能和新规则混用。

## 3. Universal Core

Universal Core 定义所有一等平台 Adapter 必须保持的商业语义：

- 参考资料接收、评级与职责分配；
- 人物身份权威和双人比例校准；
- R0–R4 用户自主精修；
- AB01–AB06 资产体系；
- 妆造、服装、道具和 Scene 语义；
- Scene → Look → Sequence → Shot 商业组片；
- Pose、Blocking、Camera Geometry、Lighting 与 Shot Intent；
- 照片生产和 Approved Shot 最终视觉基线；
- VB01 视频规划以及照片/视频共享身份资产；
- Authoritative Assets + Delta Prompt 编译；
- Scoped Revision、Regeneration、QC 和交付；
- 资产状态、依赖、失效传播和审计语义；
- 用户自主权、隐私与 Runtime Truth。

## 4. Platform Adapter

Adapter 将 Universal Core 翻译到平台真实能力。

Adapter 可以改变：

- 文件与 Runtime 结构；
- 可用工具；
- 模型路由；
- Prompt 语法；
- 参考图挂载方式；
- 持久化实现；
- 编辑、超分、视频执行路径。

Adapter 不得静默改变：

- 人物身份高保真要求；
- 用户审批门；
- 个人特征自主权；
- REJECTED / QUARANTINE 规则；
- Scoped Revision 边界；
- QC 验收标准。

这条定义为：

**Platform Adapter Non-Degradation Policy｜平台适配不降级原则**。

## 5. 当前重点 Adapter

### 小云雀

- 紧凑声明式 Skill Runtime；
- 正式 Skill 包不包含可执行脚本；
- 使用平台原生 Agent / 图片 / 视频工具，但必须经过真实能力验证；
- 必须区分 UI 可见和 Agent 可直接调用。

### 豆包

- 面向 Agent 的 Runtime；
- 在运行环境实际验证支持时，可使用确定性脚本和媒体工具；
- 工具被打包不等于可执行；
- Runtime 能力状态必须明确记录。

## 6. 能力证据状态

统一使用：

- `VERIFIED`
- `OBSERVED`
- `UNKNOWN`
- `UNSUPPORTED`
- `SUPERSEDED`

并区分：

- `UI_AVAILABLE`
- `USER_INTERACTIVE`
- `AGENT_DIRECT_CALLABLE`
- `SCRIPT_CALLABLE`

这些状态不能互相自动推导。

## 7. 版本原则

Universal Core 的版本演进与各平台 Adapter 的发行节奏相互独立。开发过程中某个 Adapter 可以暂时落后于最新 Core，但正式发布时必须说明兼容的 Core 版本和已知差异。
