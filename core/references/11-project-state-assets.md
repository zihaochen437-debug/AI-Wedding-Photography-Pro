# 项目状态、资产台账与依赖

## 1. 状态机

`DRAFT / UNDER_USER_REVIEW / REVISION_REQUIRED / APPROVED / FROZEN / SUPERSEDED / REJECTED / QUARANTINE`

只有 `APPROVED + FROZEN` 可作为正式下游权威；REJECTED/QUARANTINE 禁止继续污染生成链。

## 2. 资产依赖

`RAW REFERENCES → AB01/AB02 → AB03 → AB04/AB05 → AB06 → Blocking/Storyboard/Camera/Lighting → Photo/Video Shot → Approved Baseline → Derived Outputs`

上游改变按依赖标记 `VALID / NEEDS_REVALIDATION / INVALIDATED / SUPERSEDED`，不是无脑全项目重做。

例如 AB01 新版本使相关 AB04 与依赖 Shot 进入 NEEDS_REVALIDATION；AB06 只影响使用该 Scene 的内容；纯输出尺寸改变通常不要求重生人物。

## 3. PROJECT_STATE_SNAPSHOT

至少记录：project_id、current_phase、current_active_task、reference_intake_status、AB01–AB06 状态、current_suite/look/scene、approved_storyboard/camera/lighting/motion、photo_target_count、video_projects、active_generation_refs、last_approved_asset、open_revision、model_plan、persistence_status。

## 4. 台账

至少维护 Asset Registry、Approval Registry、Reference Manifest、Prompt Manifest、Version/Audit Log。原始用户资料与派生资产不得相互覆盖；冻结资产修改必须新版本。

## 5. 持久化

真实写入后才标 `PERSISTED`；只能当前会话则 `SESSION_ONLY`；无法确认则 `UNKNOWN`。
