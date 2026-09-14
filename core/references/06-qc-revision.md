# Ai 婚纱影像 Pro v2｜QC、证据、Scoped Revision、重生成与人工接管

## 1. HARD_FAILURE_GATE

以下属于不能交付的硬失败：

- 人物无法明确识别为本人；
- 新娘/新郎同脸、串脸、融合、身份交换；
- 明显身高、头身比或体型漂移；
- 严重手部/人体错误、肢体穿插；
- 婚纱/礼服/剧情服装未经授权改款；
- 已批准妆容未执行或妆造导致明显身份漂移；
- 关键饰品/道具错误；
- Scene 固定结构漂移；
- 明显塑料皮肤、AI 纹理崩坏；
- 配角/群演继承主角脸；
- Revision 越界修改未授权区域；
- Upscale 重绘人物/服装/Scene；
- 视频逐帧变脸、Morphing、明显穿模/漂浮、严重运镜/连续性/音画错误；
- Picture Lock 前正式生产素材存在未经要求的非剧情 BGM。

失败资产进入 `REJECTED / QUARANTINE`，禁止作为正式下游参考。

## 2. QC_DOMAINS

根据资产类型检查适用域，不为填表检查不存在的项目。

基础域：

`IDENTITY / FACE / BODY / HANDS / RETOUCH / MAKEUP / HAIR / WARDROBE / ACCESSORY / PROP_CONTACT / BLOCKING / SCENE / CAMERA / LIGHTING / COLOR / PHYSICS / TEXTURE / AI_ARTIFACTS`

视频额外：

`FRAME_IDENTITY / TEMPORAL_CONTINUITY / SCREEN_DIRECTION / EYELINE / MATCH_ON_ACTION / PROP_STATE / CAMERA_PATH / FOCUS / FLICKER / MORPHING / AV_SYNC / LIP_SYNC / DIALOGUE / AMBIENCE / FOLEY / BGM_POLICY / EDIT_RHYTHM`

## 3. QC_EVIDENCE_SCOPE

QC 结论必须与实际检查能力匹配。

允许状态：

- `PASS`：当前要求域已实际检查且通过；
- `FAIL`：有明确失败证据；
- `PARTIAL`：只检查了部分域/部分帧/部分资产；
- `NOT_VERIFIED`：当前 Runtime 无法可靠检查；
- `NOT_APPLICABLE`：该域当前任务不适用。

不得因为 Skill 写有 QC 清单就自动输出 `PASS`。

### 图片

应对实际结果图与必要 Authority/QC References 做对比。没有看到结果图时，不能宣称人物、手、妆容或服装已经通过视觉 QC。

### 视频

如果当前 Runtime 能逐帧/抽帧/时间段查看，记录实际检查范围，例如：

`0.0–8.0s full review + frame samples at 0.0/1.0/2.0...`

如果只能看到预览或无法检查全部时段，标 `PARTIAL`，不能宣称整片逐帧通过。

## 4. IDENTITY_REFERENCE_ESCALATION v2

正常生成使用最小充分当前资产，不默认把九图和所有原始图全部送入模型。

发生漂移时按问题域升级：

- 当前婚纱/剧情 Look 漂移 → 当前 Look + 对应 M01；
- 头肩/角度问题 → + 对应 U01；
- 全身/体型/肢体比例问题 → + 对应 F01；
- 眼/鼻/唇/耳/手/个人标志问题 → + 对应 D01；
- 双人身高/体型/同框比例 → + AB03-C01；
- 某真实方向持续失败 → + 该人物一张最相关的最佳真人原始证据；
- 多个下游 Shot 持续出现同类身份错误 → 回查并必要时重建当前 AB04/AB05 或 Story Look，不无限堆参考。

增加更高权威参考时替换冗余低权威项，不无限叠加。

## 5. SCOPED_REVISION_POLICY

修改什么只开放什么 + 必要最小连接区域；其他 Approved 域冻结。

例如只修新娘右手：冻结新娘脸、新郎、身高/体型、主要站位、另一只手、婚纱、新郎服装、Scene、Camera、Composition、Lighting、Color。

例如只改眼妆：只开放眼影/眼线/睫毛和必要边缘，同时保留脸型、鼻唇、肤质基线、发型、服装与 Scene。

越界：`REVISION_SCOPE_VIOLATION → FAIL`。

## 6. KNOWN_FAILURE_TARGETED_REPAIR

资产/Shot 可以维护常见失败与优先维修策略：

- 多视角板某一区域错误 → 修该区域，不重做整板；
- 婚纱披纱/头纱变肢体 → 修织物边缘和连接点；
- 双人手部粘连 → 修目标手/接触点；
- 宠物耳/爪/服装结构错误 → 只修宠物目标域；
- 前后景光学虚化像软件糊片 → 修焦平面/空间渐进，不把全图重新锐化；
- 视频局部身份错误 → 只开放目标时间段与人物身份域。

这些是问题驱动策略，不是固定 Negative 模板。

## 7. REGENERATION_FOLLOWS_ASSET_AUTHORITY

重新生成不等于重新策划。

继承仍有效的 Approved/Frozen Story、Look、Scene、DIR01、Storyboard、Camera、Lighting、Motion 和身份资产，只增加失败原因和当前 Delta。

正在重做的资产已经 `REJECTED / QUARANTINE` 时，不得继续当最高权威；执行：

`REGENERATE_FROM_NEAREST_VALID_AUTHORITY`。

## 8. RETRY_BUDGET_POLICY

商业生产允许有限目的性重试，但不能无限抽卡。

每个项目应维护：

`free_or_included_attempts / current_attempt / reason / previous_failure / changed_variable / selected_model / estimated_cost_if_known / user_cost_authorization / manual_takeover_threshold`

原则：

1. 每次重试必须知道上一版失败在哪里，以及本次改变了什么；
2. 同一 Prompt/参考/模型无变化的机械重复不算专业修复策略；
3. 优先局部 Edit / Scoped Revision，其次才是整张/整镜重生成；
4. 超过当前项目授权的费用/次数范围时重新向用户取得决定权；
5. 没有真实价格信息时不编造费用数字；
6. 具体默认次数在真实商业试运行后校准，不在 Canon 中拍脑袋固定。

## 9. MANUAL_TAKEOVER_GATE

出现以下情况之一，应建议或进入人工/用户干预，而不是后台无限循环：

- 同一硬失败在多次有针对性的修复后持续复现；
- 当前模型/工具无法满足关键身份或编辑范围；
- 平台 Runtime Capability 为 UNKNOWN/UNSUPPORTED；
- 用户要求超出当前授权成本/时长；
- 创意冲突需要用户决策；
- 视觉 QC 无法在当前 Runtime 可靠完成；
- 影片结构改变会打破 Picture Lock、声音或后期已批准状态。

人工接管不是失败；它是商业生产的正常降级路径。

## 10. UPSCALE_DIFF_GATE

超分前后比较：身份、五官、妆发、手、服装、饰品、Scene、Color、关键纹理与构图。任何无授权重绘都失败。

如果 Agent 不能直接执行/比较超分结果，标记 `NOT_VERIFIED` 并要求用户或可用工具完成验证，不假装通过。

## 11. QC RECORD

每个正式资产/Shot/Video 至少可记录：

```yaml
qc_record:
  asset_id:
  version:
  reviewed_at:
  review_method:
  domains:
  evidence_scope:
  failures:
  status:
  revision_required:
  next_action:
```

目的是让“为什么通过/为什么返修”可追溯，而不是只有一个绿色勾。