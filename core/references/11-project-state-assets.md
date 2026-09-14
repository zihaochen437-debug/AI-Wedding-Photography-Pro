# Ai 婚纱影像 Pro v2｜项目状态、生产台账与依赖

## 1. 统一状态机

所有可审批生产资产使用：

`DRAFT / UNDER_USER_REVIEW / REVISION_REQUIRED / APPROVED / FROZEN / SUPERSEDED / REJECTED / QUARANTINE`

只有 `APPROVED + FROZEN` 可作为正式下游权威；`REJECTED / QUARANTINE` 禁止继续污染生成链。

依赖健康状态独立使用：

`VALID / NEEDS_REVALIDATION / INVALIDATED / STALE / SUPERSEDED`

资产审批状态和依赖健康状态不能混为一个字段。

## 2. v2 资产依赖主链

```text
RAW REFERENCES
↓
Reference Roles + Retouch Profile + Standard Wardrobe
↓
AB01-M/U/F/D + AB02-M/U/F/D
↓
AB03-C01
↓
Phase B Work Mode + Product Branch
├─ PHOTO → AB04/AB05 → AB06 → DIR01/Blocking/Camera/Lighting → Photo Shot
├─ VF01 → Approved Wedding Photos → VP/VD/VC/VB01 → Video Shot/Take
├─ VF02 → Story → Script Breakdown → Character/Story Look/Prop/Film Scene → VD/VC/VB01 → Shot/Take
└─ VF03 → Story Assets + Wedding Assets → Bridge Map/VD/VC/VB01 → Shot/Take
↓
Approved Baseline
↓
Edit / Sound / Color / VFX / Upscale / Delivery Derivatives
↓
Final Master
```

上游改变按**真实依赖**传播，不无脑全项目重做。

## 3. 九图人物依赖传播

### M01 更新

某人物 M01 新版本被批准后：

- 该人物 U/F/D → `NEEDS_REVALIDATION`
- 依赖该人物的 AB03-C01 → `NEEDS_REVALIDATION`
- 当前 AB04/AB05 → `NEEDS_REVALIDATION`
- 使用该身份的照片/影视 Shot → 只在确实受影响时进入复核

### U/F/D 更新

只影响读取对应域的下游内容。例如只更新手部 Detail，不默认让所有环境大景失效；但手部特写、戒指/牵手 Shot 应复核。

### AB03-C01 更新

主要影响双人身高、体型、头部尺度、同框比例与 Blocking；不自动否定 AB01/02 单人面部身份。

### Retouch Profile 更新

如果用户改变人物长期精修基线，M/U/F/D 及基于该基线的当前 Look 进入 `NEEDS_REVALIDATION`；已经批准的历史成片保留为历史版本，不静默覆盖。

## 4. Look / Scene / Director 依赖

- AB04/AB05 更新 → 只影响使用该 Look 的照片/影视内容。
- AB06 更新 → 只影响使用该 Scene 的 Sequence/Shot。
- DIR01 更新 → 对尚未生成或需要重新导演的 Photo Shot 生效；历史 Approved Shot 不自动失效。
- Camera/Lighting/Motion Asset 更新 → 只影响绑定该控制资产的 Shot。

## 5. Story / Film 依赖

### Story 修改

`STORY V1 APPROVED → STORY V2` 时：

- 旧 VB01 → `STALE`
- 受变化 Beat/Scene 影响的 Script Breakdown / Character State / Prop / Film Scene → `NEEDS_REVALIDATION`
- 已生成且仍与新故事一致的 Shot 不无脑删除，但进入依赖审查

### 只改 Storyboard/Camera

Story 保持 VALID；只更新目标 VB01/Shot/Camera 版本和真实受影响下游。

### Selected Take / Edit

Take 被替换只影响 EDL 中使用该 Take 的位置。Picture Lock 后若必须改变画面结构，应重新打开 Picture Lock 状态并重新执行受影响的 Audio/Music/Color/QC，不得假装后期仍然有效。

## 6. PROJECT_STATE_SNAPSHOT

项目快照至少记录：

```yaml
project_id:
project_name: "Ai 婚纱影像 Pro"
project_version:
current_phase:
current_active_task:
persistence_status:

reference_intake_status:
retouch_profile:
standard_wardrobe:

identity_assets:
  bride:
    M01:
    U01:
    F01:
    D01:
  groom:
    M01:
    U01:
    F01:
    D01:
  couple:
    C01:

phase_b:
  work_mode:
  output_type:
  photo_target_count:
  current_suite:
  current_look:
  current_scene:

creative_assets:
  AB04:
  AB05:
  AB06:
  DIR01:
  approved_camera:
  approved_lighting:
  approved_motion:

film_projects:
  - video_id:
    product_class:
    story_autonomy:
    storyboard_autonomy:
    story_status:
    VP01:
    VS01:
    VD01:
    VC01:
    VB01:
    VSL01:
    VA01:
    EDL01:
    picture_lock:
    film_qc_status:

active_generation_refs:
qc_audit_refs:
last_approved_asset:
open_revision:
model_plan:
approval_state:
```

不适用字段可以为空，但不能因为 Compact Runtime 而丢失语义。

## 7. Production Ledgers

商业项目至少具有逻辑台账：

- `ASSET_REGISTRY`
- `APPROVAL_REGISTRY`
- `REFERENCE_MANIFEST`
- `PROMPT_MANIFEST`
- `VERSION_AUDIT_LOG`
- `MODEL_LEDGER`
- `SHOT_TAKE_LEDGER`
- `AUDIO_LEDGER`（影视适用）
- `DELIVERY_LEDGER`

这些可以由平台项目状态、结构化文件、自由画布关系或用户可验证方式实现；不能因为小云雀不允许脚本就在语义上删除台账。

## 8. Version Rules

冻结资产修改必须产生新版本；旧版本标记 `SUPERSEDED` 而不是从历史中消失。

正式槽位版本示例：

`AB01-U01-V01 → SUPERSEDED`
`AB01-U01-V02 → APPROVED + FROZEN`

修复不能通过创建新的正式槽位逃避版本关系。

## 9. Persistence Truth

只有项目状态真实写入并能恢复时标 `PERSISTED`；只能当前会话使用则 `SESSION_ONLY`；无法确认则 `UNKNOWN`。

不能因为自由画布“看起来还在”就自动声称永久持久化，也不能因为 Skill 文档描述了 Snapshot 就声称状态已经写入。

## 10. Recovery

会话/任务恢复时优先读取最近的可信 Snapshot 和已冻结资产，不重新从零策划：

`Snapshot → Validate Existing Authority → Resolve Open Revision → Resume Current Gate`

若状态来源冲突，以用户当前确认 + 最新有效版本 + 可验证平台状态为准，并显式标记待复核项。